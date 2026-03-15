from fastapi import FastAPI, HTTPException
from models import User, Product
from database import user,product
from typing import Optional



app=FlaskAPI()

@app.get("/")
def home():
    return {"message":"Welcome to user and product management API"}

@app.post("/user", Response_Model=User)
def create_user(newuser=User):
    user.append(newuser)
    return newuser

@app.get("/user/{email}",response_model=User)
def get_user(email:str):
    

