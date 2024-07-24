import streamlit as st
import pickle
import numpy as np

with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Sales Prediction App')

tv_expense = st.number_input('Enter TV Ad Expense ($)', min_value=0)
radio_expense = st.number_input('Enter Radio Ad Expense ($)', min_value=0)

if st.button('Predict Sales'):
    input_data = np.array([[tv_expense, radio_expense]])

    prediction = model.predict(input_data)
    
    st.write(f'Predicted Sales: ${prediction[0]:.2f}')

st.markdown('---')
st.markdown('**Developed by Lê Văn Trường**')
