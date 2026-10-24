from pydantic import BaseModel,EmailStr,Field
from typing import List, Dict, Optional, Annotated
#here comes the use of Annotated in which you can add constraints with metadata using field and annotations.


class Patient(BaseModel):
    name : Annotated[str,Field(max_length=50, description= "Enter your name within 50 characters")]
    email: Optional[EmailStr]=None
    age : int=Field(gt=0, lt=60) 
    weight:Annotated[float,Field(strict=True,description="Please strictly add a float value and not a string value because strict will make sure it fails to read string as float which is done by default in Pydantic")]
    contact_details:Dict[str,str]
    allergies: Annotated[Optional[List[str]],Field(default=None, max_length=50)]  


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
        "contact_details":{"phone":"9522005438","email":"abc@gmail.com"}}

patient1 = Patient(**patient_info)



insert_patient_data(patient1)