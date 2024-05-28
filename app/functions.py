from fastapi import HTTPException

def print_msg(): 
     print("test-----------")

def equation_picker(op: str, num1: int, num2: int) -> any:
    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "%": divide
    }

    if op in operators:
        return {"result" : operators[op](num1, num2)}
    else: 
        raise HTTPException(status_code=405, detail="operator was invalid")
    


def add (num1: int, num2: int) -> int:
     return num1 + num2 


def subtract (num1, num2):
     return num1 - num2 

def multiply (num1, num2):
     return num1 * num2

def divide (num1, num2):
     return num1 / num2



