import streamlit as st

def home():
    st.title("Real Estate Data Science Portfolio Project")

    st.write(
        "Welcome to my Real Estate Data Science Portfolio Project! This project focuses on real estate data analysis "
        "with a primary focus on properties in Gurgaon. I have developed an app with three main segments to showcase "
        "different aspects of the real estate market."
    )

    st.markdown("### Prediction Page")
    st.write(
        "Explore the Prediction Page to make predictions related to Gurgaon's real estate market. "
        "Use machine learning models to forecast property prices or other relevant metrics based on the provided input."
    )

    st.markdown("### Analysis Page")
    st.write(
        "The Analysis Page allows you to delve into the Gurgaon real estate dataset. Visualize key trends, analyze property features, "
        "and gain insights into the dynamics of the real estate market in Gurgaon."
    )

    st.markdown("### Recommendation Page")
    st.write(
        "In the Recommendation Page, discover personalized recommendations for Gurgaon properties based on preferences and historical data. "
        "The recommendation algorithms aim to provide tailored suggestions for potential buyers or investors in the Gurgaon market."
    )

    st.write(
        "This project is currently focused on Gurgaon property, but stay tuned! We have plans to expand our analysis to include more cities "
        "in the future. Feel free to navigate through the different segments using the sidebar navigation. "
        "Explore the features and functionalities of the Real Estate Data Science Portfolio Project!"
    )

