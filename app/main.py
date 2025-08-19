from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from psycopg2.extras import RealDictCursor
from random import randrange
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from .routers import post, user, auth

import psycopg2
import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:

    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', 
                                password = 'password123', cursor_factory = RealDictCursor)
    
        cursor = conn.cursor()

        print ("Database connection was succesfull!")
        break

    except Exception as error:
        print ("Connection to database failed")
        print ("Error: ", error)
        time.sleep(2)


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!"}