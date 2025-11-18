import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Try loading multiple pre-trained models (Logistic Regression, Random Forest, etc.)
try:
    rf_model_path = 'Randomf.sav'
    rf_model = pickle.load(open(rf_model_path, 'rb'))

    knn_model_path = 'KNN.sav'
    knn_model = pickle.load(open(knn_model_path, 'rb'))

except Exception as e:
    st.error(f"Error loading model: {e}")
    rf_model = lr_model = svm_model = dt_model = knn_model = None  # Assign None if model loading fails

# Sidebar for navigation
with st.sidebar:
    selected_model = st.selectbox('Select Model for Prediction', ['Random Forest', 'KNN'])

# Database prediction page
if selected_model:
    # Page title
    st.title(f'{selected_model} Prediction')

    # Ensure the selected model is loaded before making predictions
    if selected_model == 'Random Forest' and rf_model:
        selected_model_instance = rf_model
    
    elif selected_model == 'KNN' and knn_model:
        selected_model_instance = knn_model
    else:
        selected_model_instance = None
        st.error(f"{selected_model} model is not loaded properly. Please check the model file.")

    # Collect user inputs for each feature
    age = st.number_input('Age', min_value=0, max_value=100, value=25)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    family_history = st.selectbox('Family History of Mental Illness', ['No', 'Yes'])
    benefits = st.selectbox('Do you have Mental Health Benefits?', ['No', 'Yes'])
    care_options = st.selectbox('Do you have access to Mental Health Care?', ['No', 'Yes'])
    anonymity = st.selectbox('Do you feel anonymous when seeking care?', ['No', 'Yes'])
    leave = st.selectbox('Can you take leave from work for mental health reasons?', ['No', 'Yes'])
    work_interfere = st.selectbox('Does work interfere with your mental health?', ['No', 'Yes'])

    # Convert categorical variables to numeric values (e.g., Yes = 1, No = 0, Male = 1, Female = 0)
    gender_value = 1 if gender == 'Male' else 0
    family_history_value = 1 if family_history == 'Yes' else 0
    benefits_value = 1 if benefits == 'Yes' else 0
    care_options_value = 1 if care_options == 'Yes' else 0
    anonymity_value = 1 if anonymity == 'Yes' else 0
    leave_value = 1 if leave == 'Yes' else 0
    work_interfere_value = 1 if work_interfere == 'Yes' else 0

    # Create a DataFrame with the user inputs
    new_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_value],  # Male=1, Female=0
        "family_history": [family_history_value],  # Yes=1, No=0
        "benefits": [benefits_value],  # Yes=1, No=0
        "care_options": [care_options_value],  # Yes=1, No=0
        "anonymity": [anonymity_value],  # Yes=1, No=0
        "leave": [leave_value],  # Yes=1, No=0
        "work_interfere": [work_interfere_value]  # Yes=1, No=0
    })

    # Display the input data for review
    st.write("Input Data for Prediction:")
    st.write(new_data)

    # Make prediction when the button is pressed
    if st.sidebar.button('Predict') and selected_model_instance:
        # Use the selected model to make predictions
        prediction = selected_model_instance.predict(new_data)
        
        # Show the prediction result
        if prediction[0] == 0:
            st.success("Prediction: Not at risk")
        else:
            st.success("Prediction: At risk")
