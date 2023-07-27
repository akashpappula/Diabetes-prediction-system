# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:22:57 2023

@author: Akash Pappula
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/akash pappula/OneDrive/Documents/Models/diabetes_model.sav', 'rb'))


def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    


def main():
    
    
    #giving title 
    st.title('Diabetes Prediction Web App')
    
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Level')
    Bloodpressure=st.text_input('Blood pressure Value')
    Skinthickness=st.text_input('Skinthickness Value')
    Insuline=st.text_input('Insuline Level')
    BMI=st.text_input('BMI Value')
    DiabetespedegreeFunction=st.text_input('DiabetespedegreeFunction Value')
    Age=st.text_input('Age of the person')
    
    
    #code for prediction
    
    diagnosis=''
    
    if st.button('Diabetes test result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,Bloodpressure,Skinthickness,Insuline,BMI,DiabetespedegreeFunction,Age])
        
        
    st.success(diagnosis)
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    