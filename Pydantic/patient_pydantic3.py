from pydantic import BaseModel
from typing import List, Dict, Optional

#Define a pydantic model

class Patient(BaseModel):
    name : str
    age : int
    weight:float
    contact_details:List[str]
    allergies: Optional[Dict[str,str]]= None # a default value has to be given for applying the optional field 

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
        "contact_details":{'9522005438','abc@gmail.com'}}
#If we try and do manipulation with the data type entered, Pydantic will throw an error. How did we achieve this,
# Go to line 10 &11 for the reference we did a two step validation in which we added contact_details will be a List which 
# will have a string datatype.

        #Define object for calling the dictionary 
patient1 = Patient(**patient_info)

#calling the function

insert_patient_data(patient1)