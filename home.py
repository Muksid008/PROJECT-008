"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("A Predictive Analytics Framework for Stress Patterns: Using Machine Learning Amidst Academic Challenges And Health Impact Analysis.")

    # Add image to the home page
    st.image("./images/home.jpg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size: 18px; text-align: justify;">
  This project aims to predict student-related stress levels and patterns using machine learning (ML) models and deep learning techniques by analysing physiological, behavioural, and academic data. The system integrates self-reported surveys (study hours, sleep, exercise, etc.) with real-time wearable data (heart rate, sleep quality, activity levels) to develop a robust predictive model. To ensure a high-accuracy model, various machine learning (ML) and deep learning (DL) techniques were implemented, including XGBoost, LightGBM, and LSTM networks. The models were compared based on standard evaluation metrics such as accuracy, precision, recall, and F1-score. XGBoost performed efficiently with optimized hyperparameters but was slightly less effective in detecting complex patterns over time. LightGBM provided high-speed performance with reasonable accuracy, making it a good alternative. LSTM (Long Short-Term Memory Networks) captured temporal dependencies in stress patterns, leading to superior prediction accuracy. The best model was chosen based on accuracy and generalization performance, ensuring minimal overfitting and maximum predictive reliability. Using ML algorithms (Random Forest, SVM, XGBoost) and deep learning (LSTM for time-series analysis), the project provides real-time stress monitoring and personalized recommendations. The final accuracy of this project lies between 93% - 95% approximately.
</p>

    """, unsafe_allow_html=True)