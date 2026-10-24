from pydantic import BaseModel,EmailStr,Field,AnyUrl
#EmailStr is for making sure by pydantic that email is in the correct form
#Field is used for two purposes first is adding constraints which is done in this very file and second is adding 
#metadata using annotated which is a part of type which we will do in the next file.
from typing import List, Dict, Optional


class Patient(BaseModel):
    name : str=Field(max_length=50) # this ensures that the max length of string is 50 characters
    email: EmailStr
    age : int=Field(gt=0, lt=60) #This makes sure that the age entered is b/w 0 and 60 otherwise error
    weight:float
    contact_details:Dict[str,str]
    allergies: Optional[List[str]]= None  #Need not be entered while defining


def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.allergies)
        print(patient.contact_details)
 

patient_info= {
        "name":"Virang", 
        "age": "19",
        "weight":80.5,
        "contact_details":{'phone':'9522005438','email':'abc@gmail.com'},
        "email": "abc@gmail.com"}

patient1 = Patient(**patient_info)



insert_patient_data(patient1)