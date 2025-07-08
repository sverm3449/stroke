import numpy as np

import pickle

loading_model = pickle.load(open('D:/resolute/stroke/trained_model.sav', 'rb'))

#input_data = (age,gender,hypertension, heart_disease, ever_married, work_type,Residence_type,avg_glucose_level,bmi,smoking_status)
input_data = (85,1,1,1,1,0,0,200.45,80.4,3)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

prediction = loading_model.predict(input_data_reshaped)
print(prediction)

if (prediction == 0):
  print("The person is not having a chances of stroke")
else:
  print("The person is having a chance of stroke")