import streamlit as st

def home():
    st.title("Home Page")
    st.write(
        "Welcome to my Data Science Portfolio Project! In this project, I have created an app "
        "with different segments to showcase my skills and projects. Explore the following sections:"
    )

    st.markdown("### Prediction Page")
    st.write(
        "In the Prediction Page, you can use the app to make predictions based on the trained models. "
        "Upload your data, and the app will provide predictions using the implemented machine learning models."
    )

    st.markdown("### Analysis Page")
    st.write(
        "The Analysis Page is dedicated to exploring and analyzing the dataset. You can visualize insights, "
        "statistics, and trends to gain a better understanding of the data."
    )

    st.markdown("### Recommendation Page")
    st.write(
        "In the Recommendation Page, the app generates personalized recommendations based on the data. "
        "Explore suggestions and discover insights from the recommendation algorithms."
    )

    st.write(
        "Feel free to navigate through the different segments using the sidebar navigation. "
        "Enjoy exploring the features and functionalities of the Data Science Portfolio Project!"
    )
    st.sidebar.success("Select a page above.")

