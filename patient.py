from fastapi import FastAPI, Path
import json
#This is a small project just to test the CRUD of HTTP methods using FastAPI. This project is made to test the CRUD of HTTP methods using FastAPI.

app=FastAPI()
# Function to load data from patient.json

def load_data():
    with open("patient.json","r") as f:
        data = json.load(f)
        return data

@app.get("/")
def patient():
    return {"Patient management system API"}

@app.get("/about")
def about():
    return {"This is fully functional API for monitoring patients medical scenarios"}

#Now we have to create an endpoint to view the data fetched by the function load_data
@app.get("/view")
def view():
    data=load_data() #this actiavtes the previous function created
    return data #The returned data from the load_data function is stored in data and then returned

#Now for reaching out to a specific patient we need to develop another endpoint

@app.get("/patient/{patient_id}")


def view_patient(patient_id: str= Path(..., description='ID of the patient')):
    #We are now initialising a path function
    data= load_data()

    if patient_id in data:
        return data[patient_id]
    return "Patient does not exist"
#there is still an error in our code that when the user is not found the http code still is 200 which is a success while it should be 404 not found
#For this we have to generate another file like just for distinction of before and after


