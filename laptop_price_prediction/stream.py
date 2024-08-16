import streamlit as st
import joblib

import pandas as pd
        
# FUNCTION TO LABEL ENCODE INPUT DATA FROM THE USER
def preprocess_input(df2):
    # Define the replacement dictionary
    #replace values accordingly

    brandReplacement = {'ASUS':0,'Lenovo':1,'acer':2, 'Avita':3, 'HP':4, 'DELL':5, 'MSI':6, 'APPLE':7}
    df2.brand=df2.brand.replace(brandReplacement)

    processor_brandReplacement = {'Intel':0,'AMD':1,'M1':2}
    df2.processor_brand=df2.processor_brand.replace(processor_brandReplacement)

    processor_nameReplacement = {'Core i3':0,'Core i5':1,'Celeron Dual':2, 'Ryzen 5':3, 'Core i7':4, 'Core i9':5, 'M1':6, 'Pentium Quad':7,'Ryzen 3':8, 'Ryzen 7':9, 'Ryzen 9':10}
    df2.processor_name=df2.processor_name.replace(processor_nameReplacement)

    processor_gnrtnReplacement = {'10th':0,'Not Available':1,'11th':2, '7th':3, '8th':4, '9th':5, '4th':6, '12th':7}
    df2.processor_gnrtn=df2.processor_gnrtn.replace(processor_gnrtnReplacement)

    ram_gbReplacement = {'4 GB':0, '8 GB':1, '16 GB':2, '32 GB':3}
    df2.ram_gb=df2.ram_gb.replace(ram_gbReplacement)

    ram_typeReplacement = {'DDR4':0, 'LPDDR4':1, 'LPDDR4X':2, 'DDR5':3, 'DDR3':4, 'LPDDR3':5}
    df2.ram_type=df2.ram_type.replace(ram_typeReplacement)

    ssdReplacement = {'0 GB':0, '512 GB':1, '256 GB':2, '128 GB':2, '1024 GB':3, '2048 GB':3,'3072 GB':4   }
    df2.ssd=df2.ssd.replace(ssdReplacement)

    hddReplacement = { '1024 GB':0, '0 GB':1, '512 GB':2, '2048 GB':3}
    df2.hdd=df2.hdd.replace(hddReplacement)

    osReplacement = {'Windows':0, 'DOS':1, 'Mac':2}
    df2.os=df2.os.replace(osReplacement)

    os_bitReplacement = {'64-bit':0, '32-bit':1}
    df2.os_bit=df2.os_bit.replace(os_bitReplacement)

    graphic_card_gbReplacement = {'0 GB':0, '2 GB':1, '4 GB':2, '6 GB':3, '8 GB':4}
    df2.graphic_card_gb=df2.graphic_card_gb.replace(graphic_card_gbReplacement)

    weightReplacement = {'Casual':0, 'ThinNlight':1, 'Gaming':2}
    df2.weight=df2.weight.replace(weightReplacement)

    warrantyReplacement = {'No warranty':0, '1 year':1, '2 years':2, '3 years':3}
    df2.warranty=df2.warranty.replace(warrantyReplacement)

    TouchscreenReplacement = {'No':0, 'Yes':1}
    df2.Touchscreen=df2.Touchscreen.replace(TouchscreenReplacement)

    msofficeReplacement = {'No':0, 'Yes':1 }
    df2.msoffice=df2.msoffice.replace(msofficeReplacement)

    ratingReplacement={'2 stars':0, '3 stars':1, '4 stars':2, '5 stars':3, '1 star':4}
    df2.rating=df2.rating.replace(ratingReplacement)

    return df2



# Load your trained model
model = joblib.load('model.joblib')


#THE APP TO READ DATA
# Title
st.title('Laptop Price Prediction')

# User input

#brand details
brandOptions = ['ASUS','Lenovo','acer','Avita', 'HP','DELL','MSI', 'APPLE']
selected_brand= st.selectbox('Laptop Brand', brandOptions,key='brand')

if selected_brand == 'APPLE':
    processorOptions = ['M1']
    processorNameOptions = ['M1']
    ramOptions = ['4 GB','16 GB']
    osOptions = ['Mac']
    graphicsCardOptions = ['0 GB']
    msofficeOptions = ['No']
    TouchscreenOptions = ['No']

else:
    processorOptions = ['Intel','AMD']
    ramOptions = ['4 GB', '8 GB', '16 GB', '32 GB']
    osOptions = ['Windows', 'DOS']
    graphicsCardOptions = ['0 GB', '2 GB', '4 GB', '6 GB', '8 GB']
    msofficeOptions = ['No', 'Yes']
    TouchscreenOptions = ['No', 'Yes']

#processor
selected_processorBrand = st.selectbox('Laptop Processor', processorOptions,key='processor')

if selected_processorBrand=='AMD':
    processorNameOptions = ['Ryzen 5', 'Ryzen 3', 'Ryzen 7', 'Ryzen 9']

elif selected_processorBrand=='M1':
    processorNameOptions = ['M1']

else:
    processorNameOptions = ['Core i3', 'Core i5', 'Celeron Dual', 'Core i7','Core i9', 'Pentium Quad']


#processorName
selected_processorName = st.selectbox('Processor version', processorNameOptions,key='processorName')

#processorGeneration
processorGenerationOptions = ['10th', 'Not Available', '11th', '7th', '8th', '9th', '4th','12th']
selected_generation = st.selectbox('Processor Generation', processorGenerationOptions,key='processorGeneration')

#RAM
selected_ram= st.selectbox('RAM', ramOptions,key='RAM')

#RAM TYPE
ramTypeOptions=['DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'DDR3', 'LPDDR3']
selected_ramType = st.selectbox('RAM TYPE', ramTypeOptions,key='RAM TYPE')

#SSD
ssdOptions = ['0 GB', '512 GB', '256 GB', '128 GB', '1024 GB', '2048 GB','3072 GB']
selected_ssd= st.selectbox('SSD', ssdOptions,key='SSD')

#HDD
hddOptions = ['0 GB', '512 GB', '256 GB', '128 GB', '1024 GB', '2048 GB','3072 GB']
selected_hdd = st.selectbox('HDD', hddOptions,key='HDD')

#OS
selected_os = st.selectbox('Operating System', osOptions,key='OS')

#OS_BIT
osBitOptions = ['64-bit', '32-bit']
selected_osBit = st.selectbox('Operating System Bit', osBitOptions,key='OS_BIT')

#graphicsCard
selected_graphicsCard = st.selectbox('Graphic Card', graphicsCardOptions,key='graphicsCard')

#weight
weightOptions = ['Casual', 'ThinNlight', 'Gaming']
selected_weight = st.selectbox('Weight', weightOptions,key='weight')

#warranty
warrantyOptions = ['No warranty', '1 year', '2 years', '3 years']
selected_warranty = st.selectbox('Warranty', warrantyOptions,key='warranty')

#Touchscreen	
selected_touch = st.selectbox('Touchscreen', TouchscreenOptions,key='Touchscreen')

#msoffice	
selected_msOffice = st.selectbox('MS offic', msofficeOptions,key='msoffice')

# Perform predictions
if st.button('Predict'):

    input_data={'brand':[selected_brand], 'processor_brand':[selected_processorBrand],'processor_name':[selected_processorName], 'processor_gnrtn':[selected_generation],
       'ram_gb':[selected_ram], 'ram_type':[selected_ramType], 'ssd':[selected_ssd], 'hdd':[selected_hdd], 'os':[selected_os], 'os_bit':[selected_osBit], 'graphic_card_gb':[selected_graphicsCard],
       'weight':[selected_weight], 'warranty':[selected_warranty], 'Touchscreen':[selected_touch], 'msoffice':[selected_msOffice], 'rating':['3 stars'],
       'Number of Ratings':[0], 'Number of Reviews':[0]}
    
    input_data=pd.DataFrame(input_data)

    # Preprocess the input data (if necessary)
    processed_data = preprocess_input(input_data)
    
    # Make predictions using the loaded model
    prediction = model.predict(processed_data)

    # Display the prediction
    st.write('The projected value of the laptop is: ', prediction[0])
