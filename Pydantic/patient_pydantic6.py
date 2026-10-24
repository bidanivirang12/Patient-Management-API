#This code is written to demonstrate model validator. The motive of the code is to make an emergency contact automatically for the
#patient aboe the age of 60 should have an emergency contact stored
from pydantic import BaseModel,EmailStr,Field,model_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name : str=Field(max_length=50) 
    email: EmailStr
    age : int=Field(gt=0, lt=95) 
    weight:float
    contact_details:Dict[str,str]
    allergies: Optional[List[str]]= None  

#time to do some model_validator shit
    @model_validator(mode="after")
#Now two values have to be accessed one is class and other is the whole model not one value
#as in field validator here also cls refers to Patient class and self refers to the particular field
    def validate_emergency_contact(cls,self):
      if self.age>60 and 'emergency_contact' not in self.contact_details:
            raise ValueError('Pateints above the age of 60 must have an emergency contact')
      return self

def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.allergies)
        print(patient.contact_details)
 

patient_info= {
        "name":"Virang", 
        "email":"abc@hdfc.com",
        "age": "75",
        "weight":80.5,
        "contact_details":{'phone':'9522005438','email':'abc@gmail.com',
        "emergency_contact":"98745695"}} #if the emergency field is removed the code shall throw an error

patient1 = Patient(**patient_info)



insert_patient_data(patient1)