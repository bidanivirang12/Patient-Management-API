# This is the file for showing how field validator works. To use this we have to import a new datatype which is "field_validator"
from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name : str=Field(max_length=50) # this ensures that the max length of string is 50 characters
    email: EmailStr
    age : int=Field(gt=0, lt=60) #This makes sure that the age entered is b/w 0 and 60 otherwise error
    weight:float
    contact_details:Dict[str,str]
    allergies: Optional[List[str]]= None  

    @field_validator('email') #the field which has to be checked
    @classmethod #this is there because Pydantic expects validator method to be a class method. Normally a method inside class
    #receives the object but @classmethod receives the class(cls) method
    def email_validator(cls,value):
          valid_domains=['hdfc.com','icici.com']
          # email is in the form of abc@domain_name.com
          domain_name = value.split('@')[-1]

          #now the checker
          if domain_name not in valid_domains:
                raise ValueError("Not in valid domain")
          return value

    @field_validator('name')
    @classmethod
    def case_validator(cls,value):
          return value.upper() #Makes the name uppercase

    @field_validator('age', mode='after') #here if we make the type validator mode as before it would give error as before the 
    #type conversion the value of age is a string which is getting compared to int hence it will throw error
    @classmethod
    def age_validator(cls,value):
          if 0 < value < 100:
                return value
          else:
                raise ValueError('Enter a valid age')

def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.allergies)
        print(patient.contact_details)
 

patient_info= {
        "name":"Virang", 
        "email":"abc@hdfc.com",
        "age": "19",
        "weight":80.5,
        "contact_details":{'phone':'9522005438','email':'abc@gmail.com'}}

patient1 = Patient(**patient_info)



insert_patient_data(patient1)