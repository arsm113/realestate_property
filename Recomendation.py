import streamlit as st
import pickle
import pandas as pd
import numpy as np
# from hash_encoder import hash_encode
from sklearn.model_selection import GridSearchCV
import category_encoders as ce
from sklearn.ensemble import RandomForestRegressor
def Recomendation():
    
    # st.set_page_config(page_title="Recomend Apartments")
    df = pd.read_csv('appartments.csv').drop(22)
    df.index = df['PropertyName']
    
    location_df = pickle.load(open('location_distance.pkl', 'rb'))
    
    cosine_sim1 = pickle.load(open('cosine_sim1.pkl', 'rb'))
    cosine_sim2 = pickle.load(open('cosine_sim2.pkl', 'rb'))
    cosine_sim3 = pickle.load(open('cosine_sim3.pkl', 'rb'))
    
    
    def recommend_properties_with_scores(property_name, top_n=5):
    
        cosine_sim_matrix = 30*cosine_sim1 + 20*cosine_sim2 + 8*cosine_sim3
        # cosine_sim_matrix = cosine_sim3
    
        # Get the similarity scores for the property using its name as the index
        sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    
        # Sort properties based on the similarity scores
        sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
        # Get the indices and scores of the top_n most similar properties
        top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
        top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
        # Retrieve the names of the top properties using the indices
        top_properties = location_df.index[top_indices].tolist()
        d = df[df['PropertyName'].isin(top_properties)]['Link'].to_dict()
        # Create a dataframe with the results
        recommendations_df = pd.DataFrame({
            'PropertyName': top_properties,
            'SimilarityScore': top_scores,
            'img' : d.values()
        })
    
    
        return recommendations_df
    
    # Test the recommender function using a property name
    # recommend_properties_with_scores('Ireo Victory Valley')
    # st.dataframe(location_df)
    
    st.title('Select location and title')
    selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))
    radius = st.number_input('Radius in Kms')
    if st.button('Search'):
        result_sr = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()
        for key, value in result_sr.items():
            st.text(str(key) + '--->' + str(round(value/1000)) + 'Kms')
    
    st.title('Recommend Apartments')
    selected_apartment = st.selectbox('Select an Apartment',sorted(location_df.index.to_list()))
    
    if st.button('Recommend'):
        recomendation_df = recommend_properties_with_scores(selected_apartment)
    
        st.dataframe(recomendation_df)
        for index, row in recomendation_df.iterrows():
            link = f"[{row['PropertyName']}]({row['img']})"
            st.markdown(link, unsafe_allow_html=True)
    
            # st.markdown(f"[{row['PropertyName']}]({row['img']})")
            # st.markdown(f"[{row['PropertyName']}]({row['img']})")
