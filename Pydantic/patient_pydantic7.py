#This is the code for demo of Computed Fields
from pydantic import BaseModel,computed_field
from typing import List, Dict



class Patient(BaseModel):
    name : str
    age : int
    weight:float
    height: float
    allergies: Dict[str,str] 
    contact_details: List[str]

    #Lets do computed field which is formed by given data. This field is not entered by the user.
    @computed_field
    @property
    def calculate_bmi(self) -> float:
          bmi= (self.weight)/(self.height **2) #The formula for bmi is weight/(height)^2
          return bmi
          

def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.allergies)
        print(patient.contact_details)
        print(patient.calculate_bmi)
 

        
patient_info= {
        "name":"Virang", 
        "age": "19",
        "weight":80.5,
        "height":"1.75",
        "contact_details":{'9522005438','abc@gmail.com'},
        "allergies":{'pollen':'mild','dust':'severe'}}
 
patient1 = Patient(**patient_info)



insert_patient_data(patient1)
        
