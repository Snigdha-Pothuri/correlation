import numpy as np 
import plotly.express as px
import csv
def getDataSource(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for i in csv_reader:
            marks_in_percentage.append(float(i["Marks In Percentage"]))
            days_present.append(float(i["Days Present"]))
   return {"x":marks_in_percentage,"y":days_present} 
def findCorrelation(data_source):
    correlation=np.corrceff(data_source["x",data_source["y"]])
    print("Correlation of data is:"+correlation[0,1]) 
def setUp():
    data_path="Student Marks vs Days Present.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source) 
setUp()