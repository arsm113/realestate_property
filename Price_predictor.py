import streamlit as st
import pickle
import pandas as pd
import numpy as np
# from hash_encoder import hash_encode
from sklearn.model_selection import GridSearchCV
# import category_encoders as ce
from sklearn.ensemble import RandomForestRegressor
def Price_predictor():
    
    # st.set_page_config(page_title="Viz Demo")
    # selected_page = st.sidebar.radio("", ["Home", "Prediction", "Analysis"])
    with open('df.pkl', 'rb') as file:
        df = pickle.load(file)
    with open('pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)
    
    # st.dataframe(pipeline)
    # if selected_page=='Prediction':
    st.header('Enter your Inputs')
    cl1,cl2=st.columns(2)
    
    with cl1:
    
        property_type = st.selectbox('Property Type',['flat','house'])
    with cl2:
        sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))
    cl1, cl2 = st.columns(2)
    with cl1:
    
        bedrooms = float(st.selectbox('Select number of bedroom',sorted(df['bedRoom'].unique().tolist())))
    with cl2:
        bathroom = float(st.selectbox('Select Number of bathrooms',sorted(df['bathroom'].unique().tolist())))
    
    cl1, cl2 = st.columns(2)
    with cl1:
    
        balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
    with cl2:
        property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
    
    cl1, cl2 = st.columns(2)
    with cl1:
    
        built_up_area = float(st.number_input('Built Up Area'))
    with cl2:
        servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
    
    cl1, cl2 = st.columns(2)
    with cl1:
    
        store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
    with cl2:
        furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
    
    cl1, cl2 = st.columns(2)
    with cl1:
    
        luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    with cl2:
        floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))
    
    
    
    
    
    
    if st.button('Predict'):
        # form a dataframe
        data = [
            [property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room,
             furnishing_type, luxury_category, floor_category]]
        columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                   'agePossession', 'built_up_area', 'servant room', 'store room',
                   'furnishing_type', 'luxury_category', 'floor_category']
    
        # Convert to DataFrame
        one_df = pd.DataFrame(data, columns=columns)
    
        # st.dataframe(one_df)
    
        # predict
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = base_price - 0.22
        high = base_price + 0.22
    
        # display
        # st.text("The price of the flat is between {} Cr and {} Cr".format(round(low, 2), round(high, 2)))
        predict = st.info("The price of the flat is between {} Cr and {} Cr".format(round(low, 2), round(high, 2)))
        if predict:
            st.title("Thanks For Using Our Platform")







