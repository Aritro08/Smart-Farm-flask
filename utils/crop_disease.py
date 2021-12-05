disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry_(including_sour)___Powdery_mildew',
                   'Cherry_(including_sour)___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___Leaf_scorch',
                   'Strawberry___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

disease_remedy = {
    'Apple___Apple_scab': """ <div><h4>Crop: Apple </h4></div> <div><h4>Disease: Apple Scab</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
        <br/> 2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring.
        <br/>2. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
        <br/>3. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores.""",

    'Apple___Black_rot': """ <div><h4>Crop: Apple </h4></div> <div><h4>Disease: Black Rot</h4></div>
        <br/> Cause of disease:
        <br/><br/>Black rot is caused by the fungus Diplodia seriata (syn Botryosphaeria obtusa).The fungus can infect dead tissue as well as living trunks, branches, leaves and fruits. In wet weather, spores are released from these infections and spread by wind or splashing water.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Prune out dead or diseased branches.        
        <br/>2. Remove infected plant material from the area.
        <br/>3. Be sure to remove the stumps of any apple trees you cut down. Dead stumps can be a source of spores.""",

    'Apple___Cedar_apple_rust': """ <div><h4>Crop: Apple </h4></div> <div><h4>Disease: Cedar Apple Rust</h4></div>
        <br/> Cause of disease:
        <br/><br/>Cedar apple rust is a fungal disease that depends on two species to spread and develop. It spends a portion of its two-year life cycle on Eastern red cedar (Juniperus virginiana). 
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Since the juniper galls are the source of the spores that infect the apple trees, cutting them is a sound strategy if there aren’t too many of them.
        <br/>2. While the spores can travel for miles, most of the ones that could infect your tree are within a few hundred feet. 
        <br/>3. The best way to do this is to prune the branches about 4-6 inches below the galls.""",

    'Apple___healthy': """ <div><h4>Crop: Apple </h4></div> <div><h4>Disease: No disease</h4></div>
        <br/><br/> Your crop is healthy.""",

    'Blueberry___healthy': """ <div><h4>Crop: Blueberry </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Cherry_(including_sour)___Powdery_mildew': """ <div><h4>Crop: Cherry </h4></div> <div><h4>Disease: Powdery Mildew </h4></div>
        <br/> Cause of disease:
        <br/><br/>Podosphaera clandestina, a fungus that most commonly infects young, expanding leaves but can also be found on buds, fruit and fruit stems.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Remove and destroy sucker shoots.
        <br/>2. Keep irrigation water off developing fruit and leaves by using irrigation that does not wet the leaves. Also, keep irrigation sets as short as possible.        
        <br/>3. Follow cultural practices that promote good air circulation, such as pruning, and moderate shoot growth through judicious nitrogen management.""",

    'Cherry_(including_sour)___healthy': """ <div><h4>Crop: Cherry </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': """ <div><h4>Crop: Corn </h4></div> <div><h4>Disease: Grey Leaf Spot </h4></div>
        <br/> Cause of disease:
        <br/><br/>Gray leaf spot lesions on corn leaves hinder photosynthetic activity, reducing carbohydrates allocated towards grain fill. 
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. In order to best prevent and manage corn grey leaf spot, the overall approach is to reduce the rate of disease growth and expansion.
        <br/>2. This is done by limiting the amount of secondary disease cycles and protecting leaf area from damage until after corn grain formation.
        <br/>3. High risk factors for grey leaf spot in corn: <br/>
                    a.	Susceptible hybrid
                    b.	Continuous corn
                    c.	Late planting date
                    d.	Minimum tillage systems.""",

    'Corn_(maize)___Common_rust_': """ <div><h4>Crop: Corn(maize) </h4></div> <div><h4>Disease: Common Rust </h4></div>
        <br/> Cause of disease:
        <br/><br/>Common corn rust, caused by the fungus Puccinia sorghi, is the most frequently occurring of the two primary rust diseases of corn in the U.S., but it rarely causes significant yield losses in Ohio field (dent) corn. 
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Although rust is frequently found on corn in Ohio, very rarely has there been a need for fungicide applications. This is due to the fact that there are highly resistant field corn hybrids available and most possess some degree of resistance.
        <br/>2. However, popcorn and sweet corn can be quite susceptible. In seasons where considerable rust is present on the lower leaves prior to silking and the weather is unseasonably cool and wet, an early fungicide application may be necessary for effective disease control. Numerous fungicides are available for rust control. """,

    'Corn_(maize)___Northern_Leaf_Blight': """ <div><h4>Crop: Corn(maize) </h4></div> <div><h4>Disease: Northern Leaf Blight </h4></div>
        <br/> Cause of disease:
        <br/><br/>Northern corn leaf blight (NCLB) is a foliar disease of corn (maize) caused by Exserohilum turcicum, the anamorph of the ascomycete Setosphaeria turcica. With its characteristic cigar-shaped lesions, this disease can cause significant yield loss in susceptible corn hybrids.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Management of NCLB can be achieved primarily by using hybrids with resistance, but because resistance may not be complete or may fail, it is advantageous to utilize an integrated approach with different cropping practices and fungicides.
        <br/>2. Scouting fields and monitoring local conditions is vital to control this disease.""",

    'Grape___Black_rot': """ <div><h4>Crop: Grape </h4></div> <div><h4>Disease: Black Rot </h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. The black rot fungus overwinters in canes, tendrils, and leaves on the grape vine and on the ground. Mummified berries on the ground or those that are still clinging to the vines become the major infection source the following spring.
        <br/> 2. During rain, microscopic spores (ascospores) are shot out of numerous, black fruiting bodies (perithecia) and are carried by air currents to young, expanding leaves. In the presence of moisture, these spores germinate in 36 to 48 hours and eventually penetrate the leaves and fruit stems. 
        <br/> 3. The infection becomes visible after 8 to 25 days. When the weather is wet, spores can be released the entire spring and summer providing continuous infection.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Space vines properly and choose a planting site where the vines will be exposed to full sun and good air circulation. Keep the vines off the ground and insure they are properly tied, limiting the amount of time the vines remain wet thus reducing infection.
        <br/>2. Keep the fruit planting and surrounding areas free of weeds and tall grass. This practice will promote lower relative humidity and rapid drying of vines and thereby limit fungal infection.  
        <br/>3. Use protective fungicide sprays. Pesticides registered to protect the developing new growth include copper, captan, ferbam, mancozeb, maneb, triadimefon, and ziram. Important spraying times are as new shoots are 2 to 4 inches long, and again when they are 10 to 15 inches long.""",

    'Corn_(maize)___healthy': """ <div><h4>Crop: Corn(maize) </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Grape___Esca_(Black_Measles)': """ <div><h4>Crop: Grape </h4></div> <div><h4>Disease: Black Measles</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Black Measles is caused by a complex of fungi that includes several species of Phaeoacremonium, primarily by P. aleophilum (currently known by the name of its sexual stage, Togninia minima).
        <br/> 2. The overwintering structures that produce spores (perithecia or pycnidia, depending on the pathogen) are embedded in diseased woody parts of vines. The overwintering structures that produce spores (perithecia or pycnidia, depending on the pathogen) are embedded in diseased woody parts of vines.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Post-infection practices (sanitation and vine surgery) for use in diseased, mature vineyards are not as effective and are far more costly than adopting preventative practices (delayed pruning, double pruning, and applications of pruning-wound protectants) in young vineyards. 
        <br/>2. Sanitation and vine surgery may help maintain yields. In spring, look for dead spurs or for stunted shoots. Later in summer, when there is a reduced chance of rainfall, practice good sanitation by cutting off these cankered portions of the vine beyond the canker, to where wood appears healthy. 
        <br/>3. The fungicides labeled as pruning-wound protectants, consider using alternative materials, such as a wound sealant with 5 percent boric acid in acrylic paint (Tech-Gro B-Lock), which is effective against Eutypa dieback and Esca, or an essential oil.""",

    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': """ <div><h4>Crop: Grape </h4></div> <div><h4>Disease: Leaf Blight</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
        <br/> 2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring
        <br/>2. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
        <br/>3. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores.""",

    'Grape___healthy': """ <div><h4>Crop: Grape </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",


    'Corn_(maize)___healthy': """ <div><h4>Crop: Corn(maize) </h4></div> <div><h4>Disease: No disease</h4></div>
        <br/><br/> Your crop is healthy.""",

    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': """<div><h4> Crop : Grape </h4></div> <div><h4> Disease: Leaf Spot </h4></div>""",

    'Orange___Haunglongbing_(Citrus_greening)': """ <div><h4>Crop: Orange </h4></div> <div><h4>Disease: Citrus Greening </h4></div>
        <br/> Cause of disease:
        <br/><br/>  Huanglongbing (HLB) or citrus greening is the most severe citrus disease, currently devastating the citrus industry worldwide. The presumed causal bacterial agent affects tree health as well as fruit development.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. In regions where disease incidence is low, the most common practices are avoiding the spread of infection by removal of symptomatic trees, protecting grove edges through intensive monitoring, use of pesticides, and biological control of the vector ACP.
        <br/>2. According to Singerman and Useche (2016), CHMAs coordinate insecticide application to control the ACP spreading across area-wide neighboring commercial citrus groves as part of a plan to address the HLB disease.
        <br/>3. In addition to foliar nutritional sprays, plant growth regulators were tested, unsuccessfully, to reduce HLB-associated fruit drop (Albrigo and Stover, 2015).""",

    'Peach___Bacterial_spot': """ <div><h4>Crop: Peach </h4></div> <div><h4>Disease: Bacterial Spot </h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. The disease is caused by four species of Xanthomonas (X. euvesicatoria, X. gardneri, X. perforans, and X. vesicatoria).
        <br/> 2. All four bacteria are strictly aerobic, gram-negative rods with a long whip-like flagellum (tail) that allows them to move in water, which allows them to invade wet plant tissue and cause infection.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. The most effective management strategy is the use of pathogen-free certified seeds and disease-free transplants to prevent the introduction of the pathogen into greenhouses and field production areas. 
        <br/>2. In transplant production greenhouses, minimize overwatering and handling of seedlings when they are wet.
        <br/>3. Trays, benches, tools, and greenhouse structures should be washed and sanitized between seedlings crops.""",

    'Pepper,_bell___Bacterial_spot': """ <div><h4>Crop: Pepper </h4></div> <div><h4>Disease: Bacterial Spot </h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Bacterial spot is caused by several species of gram-negative bacteria in the genus Xanthomonas.
        <br/> 2. In culture, these bacteria produce yellow, mucoid colonies. 
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. The primary management strategy of bacterial spot begins with use of certified pathogen-free seed and disease-free transplants.
        <br/>2. The bacteria do not survive well once host material has decayed, so crop rotation is recommended. Once the bacteria are introduced into a field or greenhouse, the disease is very difficult to control.
        <br/>3. Pepper plants are routinely sprayed with copper-containing bactericides to maintain a "protective" cover on the foliage and fruit.""",

    'Peach___healthy': """ <div><h4>Crop: Peach </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Pepper,_bell___healthy': """ <div><h4>Crop: Pepper </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Potato___healthy': """ <div><h4>Crop: Potato </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Raspberry___healthy': """ <div><h4>Crop: Raspberry </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Soybean___healthy': """ <div><h4>Crop: Soyabean </h4></div> <div><h4>Disease: No disease </h4></div>
        <br/><br/> Your crop is healthy.""",

    'Strawberry___healthy': """ <div><h4>Crop: Strawberry </h4></div> <div><h4>Disease: No disease</h4></div>
        <br/><br/> Your crop is healthy.""",

    'Tomato___healthy': """ <div><h4>Crop: Tomato </h4></div><div><h4>Disease: No disease</h4></div>
        <br/><br/> Your crop is healthy.""",

    'Potato___Early_blight': """ <div><h4>Crop: Potato </h4></div><div><h4>Disease: Early Blight</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Early blight (EB) is a disease of potato caused by the fungus Alternaria solani. It is found wherever potatoes are grown. 
        <br/> 2. The disease primarily affects leaves and stems, but under favorable weather conditions, and if left uncontrolled, can result in considerable defoliation.
        <br/> 3. Primary infection is difficult to predict since EB is less dependent upon specific weather conditions than late blight.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Follow a complete and regular foliar fungicide spray program.
        <br/>2. Practice good killing techniques to lessen tuber infections.
        <br/>3. Allow tubers to mature before digging, dig when vines are dry, not wet, and avoid excessive wounding of potatoes during harvesting and handling.""",

    'Potato___Late_blight': """ <div><h4>Crop: Potato </h4></div><div><h4>Disease: Late Blight</h4></div>
        Late blight is a potentially devastating disease of potato, infecting leaves, stems and fruits of plants. The disease spreads quickly in fields and can result in total crop failure if untreated.               
        <br/> Cause of disease:
        <br/><br/> 1. Late blight is caused by the oomycete Phytophthora infestans. Oomycetes are fungus-like organisms also called water molds, but they are not true fungi.
        <br/> 2. There are many different strains of P. infestans. These are called clonal lineages and designated by a number code (i.e. US-23). 
        <br/> 3. The host range is typically limited to potato and tomato, but hairy nightshade is a closely related weed that can readily become infected and may contribute to disease spread.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Seed infection is unlikely on commercially prepared tomato seed or on saved seed that has been thoroughly dried.
        <br/>2. Inspect tomato transplants for late blight symptoms prior to purchase and/or planting, as tomato transplants shipped from southern regions may be infected
        <br/>3. If infection is found in only a few plants within a field, infected plants should be removed, disced-under, killed with herbicide or flame-killed to avoid spreading through the entire field.""",

    'Squash___Powdery_mildew': """ <div><h4>Crop: Squash </h4></div><div><h4>Disease: Powdery mildew</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Powdery mildew infections favor humid conditions with temperatures around 68-81° F
        <br/> 2. In warm, dry conditions, new spores form and easily spread the disease.
        <br/> 3. Symptoms of powdery mildew first appear mid to late summer in Minnesota.  The older leaves are more susceptible and powdery mildew will infect them first.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Apply fertilizer based on soil test results. Avoid over-applying nitrogen.
        <br/>2. Provide good air movement around plants through proper spacing, staking of plants and weed control.
        <br/>3. Once a week, examine five mature leaves for powdery mildew infection. In large plantings, repeat at 10 different locations in the field.""",

    'Strawberry___Leaf_scorch': """ <div><h4>Crop: Strawberry </h4></div> <div><h4>Disease: Leaf Scorch</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Scorched strawberry leaves are caused by a fungal infection which affects the foliage of strawberry plantings. The fungus responsible is called Diplocarpon earliana.
        <br/> 2. Strawberries with leaf scorch may first show signs of issue with the development of small purplish blemishes that occur on the topside of leaves.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Since this fungal pathogen over winters on the fallen leaves of infect plants, proper garden sanitation is key.
        <br/>2. This includes the removal of infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants. 
        <br/>3. The avoidance of waterlogged soil and frequent garden cleanup will help to reduce the likelihood of spread of this fungus.""",

    'Tomato___Bacterial_spot': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Bacterial Spot</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. The disease is caused by four species of Xanthomonas.
        <br/> 2. All four bacteria are strictly aerobic, gram-negative rods with a long whip-like flagellum (tail) that allows them to move in water, which allows them to invade wet plant tissue and cause infection.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. The most effective management strategy is the use of pathogen-free certified seeds and disease-free transplants to prevent the introduction of the pathogen into greenhouses and field production areas. 
        <br/>2. In transplant production greenhouses, minimize overwatering and handling of seedlings when they are wet.
        <br/>3. Trays, benches, tools, and greenhouse structures should be washed and sanitized between seedlings crops.""",

    'Tomato___Early_blight': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Early Blight</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Early blight can be caused by two different closely related fungi, Alternaria tomatophila and Alternaria solani.
        <br/> 2. Alternaria tomatophila is more virulent on tomato than A. solani, so in regions where A. tomatophila is found, it is the primary cause of early blight on tomato. 
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>2. Rotate out of tomatoes and related crops for at least two years.
        <br/>3. Control susceptible weeds such as black nightshade and hairy nightshade, and volunteer tomato plants throughout the rotation.
        <br/>4. Fertilize properly to maintain vigorous plant growth. Particularly, do not over-fertilize with potassium and maintain adequate levels of both nitrogen and phosphorus.""",

    'Tomato___Late_blight': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Late Blight</h4></div>    
        <br/> Cause of disease:
        <br/><br/> 1. Late blight is caused by the oomycete Phytophthora infestans. Oomycetes are fungus-like organisms also called water molds, but they are not true fungi.
        <br/> 2. There are many different strains of P. infestans. These are called clonal lineages and designated by a number code (i.e. US-23). Many clonal lineages affect both tomato and potato, but some lineages are specific to one host or the other.
        <br/> 3. The host range is typically limited to potato and tomato, but hairy nightshade (Solanum physalifolium) is a closely related weed that can readily become infected and may contribute to disease spread. """,

    'Tomato___Leaf_Mold': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Leaf Mold</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Leaf mold is caused by the fungus Passalora fulva. It is not known to be pathogenic on any plant other than tomato.
        <br/> 2. Leaf spots grow together and turn brown. Leaves wither and die but often remain attached to the plant.
        <br/> 3. Fruit infections start as a smooth black irregular area on the stem end of the fruit. As the disease progresses, the infected area becomes sunken, dry and leathery.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Use drip irrigation and avoid watering foliage.
        <br/>2. Stake, string or prune to increase airflow in and around the plant.
        <br/>3. Sterilize stakes, ties, trellises etc. with 10 percent household bleach or commercial sanitizer.
        <br/>4. Remove crop residue at the end of the season. Burn it or bury it away from tomato production areas.""",

    'Tomato___Septoria_leaf_spot': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Leaf Spot</h4></div>
        <br/> Cause of disease:
        <br/><br/> Septoria leaf spot is caused by a fungus, Septoria lycopersici. It is one of the most destructive diseases of tomato foliage and is particularly severe in areas where wet, humid weather persists for extended periods.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Remove diseased leaves.
        <br/>2. Improve air circulation around the plants.
        <br/>3. Mulch around the base of the plants.""",

    'Tomato___Spider_mites Two-spotted_spider_mite': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Two-spotted spider mite</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. The two-spotted spider mite is the most common mite species that attacks vegetable and fruit crops.
        <br/> 2. They have up to 20 generations per year and are favored by excess nitrogen and dry and dusty conditions.
        <br/> 3. Outbreaks are often caused by the use of broad-spectrum insecticides which interfere with the numerous natural enemies that help to manage mite populations. 
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Avoid early season, broad-spectrum insecticide applications for other pests.        
        <br/>2. Overhead irrigation or prolonged periods of rain can help reduce populations.""",

    'Tomato___Target_Spo': """ <div><h4>Crop: Tomato </h4></div> <div><h4>Disease: Target Spot</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. The fungus causes plants to lose their leaves; it is a major disease. If infection occurs before the fruit has developed, yields are low.
        <br/> 2. This is a common disease on tomato in Pacific island countries. The disease occurs in the screen house and in the field.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Remove a few branches from the lower part of the plants to allow better airflow at the base
        <br/>2. Remove and burn the lower leaves as soon as the disease is seen, especially after the lower fruit trusses have been picked.
        <br/>3. Do not use overhead irrigation; otherwise, it will create conditions for spore production and infection.""",

    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': """ <div><h4>Crop: Tomato </h4></div><div><h4>Disease: Yellow Leaf Curl Virus</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. TYLCV is transmitted by the insect vector Bemisia tabaci in a persistent-circulative nonpropagative manner. The virus can be efficiently transmitted during the adult stages.
        <br/> 2. This virus transmission has a short acquisition access period of 15–20 minutes, and latent period of 8–24 hours.
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Currently, the most effective treatments used to control the spread of TYLCV are insecticides and resistant crop varieties.
        <br/>2. The effectiveness of insecticides is not optimal in tropical areas due to whitefly resistance against the insecticides; therefore, insecticides should be alternated or mixed to provide the most effective treatment against virus transmission.
        <br/>3. Other methods to control the spread of TYLCV include planting resistant/tolerant lines, crop rotation, and breeding for resistance of TYLCV.""",

    'Tomato___Tomato_mosaic_virus': """ <div><h4>Crop: Tomato </h4></div><div><h4>Disease: Mosaic Virus</h4></div>
        <br/> Cause of disease:
        <br/><br/> 1. Tomato mosaic virus and tobacco mosaic virus can exist for two years in dry soil or leaf debris, but will only persist one month if soil is moist. The viruses can also survive in infected root debris in the soil for up to two years.
        <br/> 2. Seed can be infected and pass the virus to the plant but the disease is usually introduced and spread primarily through human activity. The virus can easily spread between plants on workers' hands, tools, and clothes. 
        <br/> 3. The virus can even survive the tobacco curing process, and can spread from cigarettes and other tobacco products to plant material handled by workers after a cigarette
        <br/><br/> How to prevent/cure the disease: <br/>
        <br/>1. Inspect transplants prior to purchase. Choose only transplants showing no clear symptoms.
        <br/>2. Avoid planting in fields where tomato root debris is present, as the virus can survive long-term in roots.
        <br/>3. Wash hands with soap and water before and during the handling of plants to reduce potential spread between plants."""
}