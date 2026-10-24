#This api is made to make make an endpoint when the user clicks Hello World is visible.
from fastapi import FastAPI

#App object is created of FastAPI class. This object will be used to create 
# the endpoints of the api.
app = FastAPI()

@app.get("/") # the path is defined (with the help of a decorator a route is created called /)
# Here the meaning of / is that it is the root endpoint of the api. 
# When the user visits the root endpoint, the function home() will be executed. and this api 
# will be triggered and the user will see the message "Hello FastAPI!".

#Now for this endpoint 
def home():
    return {"message": "Hello FastAPI!"}

#now another endpoint we will create(An endpoint is basically the route which is created to handle a particular type of HTTP request by the user)
@app.get("/about")
def about():
    return  "This is my first api using FastAPI!"