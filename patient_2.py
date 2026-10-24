from fastapi import FastAPI, Path,HTTPException,Query
import json
#This is the SECOND PART OF THE ACTUAL CODE WHICH WAS DEVELOPED FOR THE API
#THIS INCLUDES THE THINGS OF AND AFTER HTTP STATUS CODES. FOR THIS 
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
    data=load_data() #this activates the previous function created
    return data #The returned data from the load_data function is stored in data and then returned

#Now for reaching out to a specific patient we need to develop another endpoint 

#this is functioning of path parameter

@app.get("/patient/{id}")
def view_patient(id: str= Path(..., description='ID of the patient')):
    #We are now initialising a path function
    data= load_data()

    for patient in data:
        if patient["id"]==id:
            return patient
        
    raise HTTPException(status_code=404, detail='Patient not found')

#Now for working of query parameter with which we can sort,filter or search

#creating a new endpoint
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sorting of the patients on the basis of height_cm,weight_kg or bmi"
    ),
    order: str = Query(
        "asc",
        description="Sort in ascending or descending order")):
    
    # These are the fields we are allowing to sort
    
    valid_fields = ["height_cm","weight_kg","bmi"]


#Checking whether the user entered a valid field or not

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,
                            detail=f"Invalid input. Please enter from {valid_fields}")
    #Here this f is used directly to insert valid_fields data into a string format.

    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400,
                            detail="Invalid order print from asc or desc")
    #both detail and description works

    #loading data
    data= load_data()

   

    #new variable created to identify the order entered by the user.
    sort_order = True if order=="desc" else False

    #Take all the patients, look at the field the user asked to sort by,
    #and arrange the patients according to that field.
    sorted_data= sorted(
        data.values(), 
        key=lambda x: x.get(sort_by,0),
        reverse=sort_order)
    #THE ERROR HAPPENED HERE WHERE I TREATED A DICTIONARY AS LIST, DICTIONARY SYNTAX WAS data.values() and whereas the list syntax is data or data[0]
    # This line basically means that take a look at all the pateints and field by which the user
    #has asked the sorting.
    #BREAKING DOWN THE CODE
    # data :- This means give me the data only and not P001,P002 etc
    #sorted(): arranges the data in a particular order
    #sorted(data.values()) does the sorting for the data by default true means descending and false means ascending. 
    # key=lambda x: x.get(sort_by,0 ) is basically somewhat like 
# def something(x):
# return x.get(sort_by,0) where x represents one patient at a time.
    return sorted_data