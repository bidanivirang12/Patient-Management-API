#This is to demo the Nested model concept and how to export it to python dictionary and json is also done
from pydantic import BaseModel

class Address(BaseModel):
    #the reason for creating this is stated below after gender
    house_no: int
    pin:int
    street:str

class Patient(BaseModel):
    name:str
    age:int
    gender:str

    #Now to store the address what is the datatype, address is consists of mixed types of data and for retireving one piece of info
    #It is not feasible to print that. That is why the solution is to create a seperate class for 'Address'

    address: Address
     #this is where another model is treated as field for this model
address_dict={'house_no':'02', 
                  'pin': '110010',
                  'street':'gurgaon'}
address1 = Address(**address_dict)

patient_dict={'name':'Virang',
                  'age':19,
                  'gender':'male',
                  'address':address1
                  }
patient1= Patient(**patient_dict)

# Now let's come to exporting it to dictionary
#Converting the already existing pydantic model to dictionary by using a temporary variable
temp=patient1.model_dump()

print(temp)
print(type(temp)) #we can see through this and if we wnat to convert to json then we have model_dump_json for the same
# In python it is taken as string

# we can also export selective fields
# creating another var

shark=patient1.model_dump_json(include=['name','age']) # we can also use exclude for preventing desired fields from exporting
# we can also exclude parts of the fields like using exclude={'address':['street']}
print(shark)
print(type(shark))

# there is one more thing called exclude_unset=True which rm the values which are not set by the user and default values were given
#it completely ignores them