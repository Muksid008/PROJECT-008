"""This module contains the visualization page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
import streamlit as st

# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function creates the visualization page"""
    
    # Remove warnings
    warnings.filterwarnings('ignore')

    # Set the page title
    st.title("Visualize the Stress Patterns.")

    # Correlation Heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.iloc[:, 1:].corr(), annot=True, ax=ax)
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)  # Adjust heatmap margins
        st.pyplot(fig)

    # Scatter Plots
    if st.checkbox("Show Scatter Plot"):
        st.subheader("Scatter Plots")
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))

        sns.scatterplot(ax=axes[0, 0], data=df, x='bt', y='rr')
        axes[0, 0].set_title("Body Temperature vs Respiration Rate")

        sns.scatterplot(ax=axes[0, 1], data=df, x='sr', y='lm')
        axes[0, 1].set_title("Snoring Rate vs Limb Movement")

        sns.scatterplot(ax=axes[1, 0], data=df, x='bo', y='bt')
        axes[1, 0].set_title("Blood Oxygen vs Body Temperature")

        sns.scatterplot(ax=axes[1, 1], data=df, x='sh', y='hr')
        axes[1, 1].set_title("Sleeping Hour vs Heart Rate")

        st.pyplot(fig)  # Pass the figure explicitly

    # Boxplot
    if st.checkbox("Display Boxplot"):
        st.subheader("Boxplot of Features")
        fig, ax = plt.subplots(figsize=(15, 5))
        df.boxplot(['sr', 'rr', 'bt', 'rem', 'bo', 'sh'], ax=ax)
        st.pyplot(fig)

    # Pie Chart for Stress Levels
    if st.checkbox("Show Sample Results"):
        st.subheader("Stress Level Distribution")
        stress_levels = ['Safe', 'Low', 'Medium', 'High', 'Very High']
        stress_counts = [(df['sl'] == i).sum() for i in range(5)]
        colors = sns.color_palette('pastel')[0:5]

        fig, ax = plt.subplots()
        ax.pie(stress_counts, labels=stress_levels, colors=colors, autopct='%.0f%%')
        st.pyplot(fig)
