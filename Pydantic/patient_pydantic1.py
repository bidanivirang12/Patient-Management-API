from pydantic import BaseModel
from typing import List, Dict

#Define a pydantic model

class Patient(BaseModel):
    name : str
    age : int
    weight:float
    allergies: Dict[str,str] #Assume this to be a real dictionary which has two parts a word and its meaning. Whose datatype is str
    contact_details: List[str] #Assume it to be a shopping list it has contents as apple,banana etc and the datatype is str

#Creating a function to insert patient data

def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.allergies)
        print(patient.contact_details)
 

        #Define data dictionary
patient_info= {
        "name":"Virang", 
        "age": "19",
        "weight":80.5,
        "contact_details":{'9522005438','abc@gmail.com'},
        "allergies":{'pollen':'mild','dust':'severe'}}
#If we try and do manipulation with the data type entered, Pydantic will throw an error. How did we achieve this,
# Go to line 10 &11 for the reference we did a two step validation in which we added contact_details will be a List which 
# will have a string datatype.

        #Define object of the Patient class for calling the dictionary  
patient1 = Patient(**patient_info)

#calling the function

insert_patient_data(patient1)
#Now sometimes the data which is required is not necessarily required to enter for that we use Optional module in the next file.
        
