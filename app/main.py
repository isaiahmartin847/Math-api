from fastapi import FastAPI
from functions import print_msg


app = FastAPI()


print_msg()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the simple math api",
        "how to": "got to /math/[number]/[operator]/[number] then it will return the value"
        }

@app.get("/math/{num1}/{op}/{num2}")
def math_root(op: str, num1: int, num2: int):
    return 1
    # return equation_picker(op, num1, num2)
