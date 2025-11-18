import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

mental_health = pickle.load(open('Staking.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Mental Health Prediction',
                           ['logistic Rigrassion',
                            'KNN',
                            'Random Forest',
                            'Boosting'],
                            default_index=0)
    