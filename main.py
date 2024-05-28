from fastapi import FastAPI, HTTPException


app = FastAPI

@app.get("/")
def home_root (): 
    return {"this is": "home"}