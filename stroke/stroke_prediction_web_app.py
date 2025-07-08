
from turtle import width
from matplotlib.ft2font import BOLD
import numpy as np
import pickle
import streamlit as st
from PIL import Image
from traitlets import default

loading_model = pickle.load(open('D:/resolute/stroke/trained_model.sav', 'rb'))



st.image("logo.png")


def stroke_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

    prediction = loading_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction == 0):
        return "The person is not having a chances of stroke"
    else:
        return "The person is having a chance of stroke"

def main():
    st.title('Stroke Prediction')

    
    age = st.text_input("Age",key="age")
    #age = st.number_input(label='enter Age',)
    Avg_Glucose_level = st.text_input("Glucose level")
    bmi = st.text_input("BMI")
    gender = st.selectbox('Gender', ['<select>','Male','Female'],0)
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    hypertension = st.selectbox('Hypertension', ['<select>','Yes','No'],0)
    if hypertension == "Yes":
        hypertension = 1
    else:
        hypertension = 0
    Heart_disease = st.selectbox('Heart Disease', ['<select>','Yes','No'],0)
    if Heart_disease == "Yes":
        Heart_disease = 1
    else:
        Heart_disease = 0
    Married = st.selectbox('Married', ['<select>','Yes','No'],0)
    if Married == "Yes":
        Married = 1
    else:
        Married = 0
    work_tpye = st.selectbox('Work type', ['<select>','Govt job' ,'Never worked', 'Private', 'Self-employed' ,'children'],0)
    if work_tpye == "Govt job":
        work_tpye = 0
    if work_tpye=="Never worked":
        work_tpye = 1
    if work_tpye == "Private":
        work_tpye=2
    if work_tpye=="Self Employed":
        work_tpye=3
    else:
        work_tpye=4
    Residence_type = st.selectbox('Residence type', ['<select>','Rural','Urban'],0)
    if Residence_type == "Rural":
        Residence_type = 0
    else:
        Residence_type = 1
    
    #bmi = st.number_input(label='enter bmi')
    smoking_status = st.selectbox('Smoking Status', ['<select>','Unknown' ,'formerly smoked' ,'never smoked', 'smokes'],0)
    if smoking_status == "Unknown":
        smoking_status = 0
    if smoking_status == "Formerly smoked":
        smoking_status=1
    if smoking_status=="Never Smoked":
        smoking_status=2
    else:
        smoking_status=3


    Diagnosis = ''

    if st.button("prediction Result"):
        Diagnosis = stroke_prediction([age, gender,hypertension,Heart_disease,Married,work_tpye,Residence_type,Avg_Glucose_level,bmi,smoking_status])


    st.success(Diagnosis)

if __name__ == '__main__':
    main()

    

