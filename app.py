import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

#loadinf the save model

mental_health = pickle.load(open('/home/panda/Desktop/DMML Project/Staking.sav'))

#slide bar navigation


with at.sidebar:
    selected = option_menu('Mental Health Prediction',
                           ['logistic Rigrassion',
                            'KNN',
                            'Random Forest',
                            'Boosting'].
                            default_index =0)
    