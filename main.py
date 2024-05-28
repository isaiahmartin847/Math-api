from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the simple math api",
        "how to": "got to /math/[number]/[operator]/[number] then it will return the value"
        }