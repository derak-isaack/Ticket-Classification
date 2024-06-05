import streamlit as st  
import joblib  

with open('xgb_ticket.pkl','rb') as f:
    model = joblib.load(f)
    
st.set_page_config(page_title='Ticket Price Prediction', page_icon=':ticket:')

st.title("Customer complaints classification")