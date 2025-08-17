"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Configure the app (MUST be the first Streamlit command)
st.set_page_config(
    page_title='A Predictive Analytics Tool.',
    page_icon='🔥',  # Used an emoji as a page icon
    layout='wide',
    initial_sidebar_state='auto'
)

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise

# Dictionary for pages
Tabs = {
    "🛖 Home": home,
    "🤪 Data Info": data,
    "⛺️ Prediction": predict,
    "🌈 Visualisation": visualise
}

# Create a sidebar
st.sidebar.title("DIRECTORY.")

# Create radio option to select the page
page = st.sidebar.radio("Start Exploring Modules", list(Tabs.keys()))

# Loading the dataset (Using caching to prevent reloading)
df, X, y = load_data()  # The cache is now handled inside `load_data()`

# Call the app function of the selected page
if page in ["⛺️ Prediction", "🌈 Visualisation"]:
    Tabs[page].app(df, X, y)
elif page == "🤪 Data Info":
    Tabs[page].app(df)
else:
    Tabs[page].app()
