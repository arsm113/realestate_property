# main.py
import streamlit as st
from home import home
from Price_predictor import Price_predictor
from Analysis_app import Analysis_app
from Recomendation import Recomendation

# Create a dictionary to map page names to their respective functions
pages = {
    "Home": home,
    "Prediction": Price_predictor,
    "Analysis": Analysis_app,
    "Recommendation": Recomendation,
}

# Streamlit app
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Call the selected page function
    pages[selection]()

if __name__ == "__main__":
    main()

