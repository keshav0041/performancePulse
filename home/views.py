import csv
from django.shortcuts import render
from .models import *
import pandas as pd
import numpy as np
import joblib 
# Create your views here.
def home(request):
    return render(request,"pages/login.html",{})

def registration(request):
    return render(request,'pages/registration-validation.html')

def dashboard(request):
    return render(request,'pages/result.html')

     

def fileupload(request):
    if request.method =="POST":
        csv_file = request.FILES.get('csv_file')
        out = pd.read_csv(csv_file)

        # Load the machine learning model
        model_predict = joblib.load('E:/Django/abx/projectCSV/Ml_Model/model1.pkl')
        knn_model_classify = joblib.load('E:/Django/abx/projectCSV/Ml_Model/model2.pkl')

        data = {'ENROLLMENTNUMBER': [], 'Attendance': [], 'CGPA': [], 'performance': [], 'category':[] } 
        df = pd.DataFrame(data)
        
        #predict for each row in csv 
        for index, row in out.iterrows():
                new_student_data = np.array([[row['CGPA'],row['Attendance']]])
                predicted_performance = model_predict.predict(new_student_data)
                predicted_category = knn_model_classify.predict(new_student_data)
                df = df.append({'ENROLLMENTNUMBER':row['ENROLLMENTNUMBER'], 'Attendance': row['Attendance'],'CGPA': row['CGPA'],          'performance': predicted_performance, 'category':predicted_category}, ignore_index=True)

        predictions = df.copy(deep=True)

        return render(request, 'pages/prediction_result.html', {'predictions': predictions})
    
    return render(request,'pages/fileupload.html')
