from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, computed_field
from typing import Annotated
import json

app = FastAPI()


def load_data():
    with open("patient.json","r") as f:
        data=json.load(f)
        return data
    
class Patient(BaseModel):
    name: str
    id: Annotated[str, Field(..., description='ID of the patient')]
    age: Annotated[int, Field(gt=0, lt=100)] #This is somewhat like age : int= Field(gt=0,lt=100) but the way in code is recommended
    gender: Annotated[str, Field(description="Gender of the patient")]
    city: str
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal weight"
        elif self.bmi < 30:
            return "Overweight"
        return "Obese"


@app.post("/create")
#The data given in the json file is sent to pydantic model for validation which is Patient model
def create_patient(patient: Patient):
    # Load existing patient data
    data=load_data()
    

    # Check whether patient already exists
    if patient.id in data:
        raise HTTPException(
            status_code=409,
            detail="Patient already exists"
        )

    # Add the new patient
    #Patient is a pydantic object so it is converting to a standard python dictionary.
    data[patient.id] = patient.model_dump()

    # Save updated data
    with open("patient.json", "w") as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Patient created successfully",
        "patient": patient
    }
