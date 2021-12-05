from os import stat
from flask import Flask, render_template, request, Markup
from flask.helpers import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_cors import CORS
from joblib import load
from torchvision import transforms
from PIL import Image
from models.disease_model import ResNet9
from utils.crop_disease import disease_classes
from utils.crop_disease import disease_remedy
from utils.fert_display import fert_practices
import torch
import io
import statistics
import requests
import numpy as np

app = Flask(__name__, static_folder='smart-farm-template/build', static_url_path='')

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/smart_farm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Rainfall(db.Model):
    __tablename__ = 'rainfalldata'
    id = db.Column(db.Integer, primary_key=True)
    state_ut_name = db.Column(db.String(200))
    district = db.Column(db.String(200))
    rabi_months = db.Column(db.Float)
    kharif_months = db.Column(db.Float)

    def __init__(self, state_ut_name, district, rabi_months, kharif_months):
        self.state_ut_name = state_ut_name
        self.district = district
        self.rabi_months = rabi_months
        self.kharif_months = kharif_months

class Nutrients(db.Model):
    __tablename__ = 'soildata'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(200))
    district = db.Column(db.String(200))
    N = db.Column(db.Float)
    P = db.Column(db.Float)
    K = db.Column(db.Float)

    def __init__(self, state, district, N, P, K):
        self.state = state
        self.district = district
        self.N = N
        self.P = P
        self.K = K

api_key = "78e9575306ac9a898d20b6f7d67250f4"

crop_model = load('./models/crop_pipeline.joblib')
fert_model = load('./models/fertilizer_pipeline.joblib')
disease_model_params = './models/plant-disease-model.pth'

disease_model = ResNet9(3, len(disease_classes))
disease_model.load_state_dict(torch.load(
    disease_model_params, map_location=torch.device('cpu')))
disease_model.eval()

def weather_fetch(city_name, api_key=api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        req_data = weather_data["main"]
        temperature = round((req_data["temp"] - 273.15), 2)
        humidity = req_data["humidity"]
        return temperature, humidity
    else:
        return None

def geocode_fetch(city_name, api_key=api_key):
    base_url = "http://api.openweathermap.org/geo/1.0/direct?"
    complete_url = base_url + "q=" + city_name + "&limit=1" + "&appid=" + api_key
    res = requests.get(complete_url)
    geo_data = res.json()

    if geo_data:
        geo_data = geo_data[0]
        return geo_data['lat'], geo_data['lon']
    else:
        return None 

def predict_image(img, model=disease_model):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.ToTensor(),
    ])
    image = Image.open(io.BytesIO(img))
    img_t = transform(image)
    img_u = torch.unsqueeze(img_t, 0)

    yb = model(img_u)

    _, preds = torch.max(yb, dim=1)
    prediction = disease_classes[preds[0].item()]
    
    return prediction

@app.route('/crop-predict', methods = ['POST'])
def cropPredict():
    data = request.json
    if data:
        state = data['state'].lower()
        district = data['district'].lower()
        soil_type = data['soilType']
        season = data['season']

        if weather_fetch(state) != None:
            temperature, humidity = weather_fetch(state)
            rainfall = N = P = K = 0
            rainfall_data = db.session.query(Rainfall.kharif_months, Rainfall.rabi_months).filter(
                or_(
                    Rainfall.state_ut_name == state, 
                    Rainfall.district == district
                )).all()
            if rainfall_data:
                rainfall_data = [x._asdict() for x in rainfall_data][0]
                if season == 'rabi':
                    rainfall = rainfall_data['rabi_months']
                else:
                    rainfall = rainfall_data['kharif_months']
            soil_data = db.session.query(Nutrients.N, Nutrients.P, Nutrients.K).filter(
                or_(
                    Nutrients.state == state, 
                    Nutrients.district == district
                )).all()
            if soil_data:
                soil_data = [x._asdict() for x in soil_data][0]
                N, P, K = soil_data['N'], soil_data['P'], soil_data['K']
            
            test_data = np.array([[N, P, K, temperature, humidity, rainfall]])
            
        try:
            result_crop = crop_model.predict(test_data)[0]
            return {'crop': result_crop}
        except:
            return {'error': 'An error occcured. Please try again'}

    return {'error': 'An error occcured. Please try again'}

@app.route('/fertilizer-predict', methods = ['POST'])
def fertPredict():
    data = request.json
    if data:
        state = data['state'].lower()
        district = data['district'].lower()
        soil_type = data['soilType']
        crop_type = data['cropType']

        if weather_fetch(state) != None:
            temperature, humidity = weather_fetch(state)
            N = P = K = 0
            soil_data = db.session.query(Nutrients.N, Nutrients.P, Nutrients.K).filter(
               or_(
                   Nutrients.state == state,
                   Nutrients.district == district
               )).all()
            if soil_data:
                soil_data = [x._asdict() for x in soil_data][0]
                N, P, K = soil_data['N'], soil_data['P'], soil_data['K']
            lat, lon = geocode_fetch(state)
            test_data = np.array([[temperature, humidity, soil_type, crop_type, N, P, K]])

        try:
            result_fert = fert_model.predict(test_data)[0]
            return {'fert': fert_practices[result_fert]}
        except:
            return {'error': 'An error occcured. Please try again'}

    return {'error': 'An error occcured. Please try again'}

@app.route('/disease-predict', methods = ['POST'])
def diseasePredict():
    if request.files:
        image = request.files.get('file').read()
        pred = predict_image(image)
        remedy = Markup(str(disease_remedy[pred]))

        return {'pred': pred, 'remedy': remedy}
    
    return {'error': 'An error occcured. Please try again'}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()