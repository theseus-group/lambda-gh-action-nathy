import random
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# Change this number as needed
MAX_RANDOM_NUMBER = 100

@app.get("/")
def get_random_number():
    random_number = random.randint(0, MAX_RANDOM_NUMBER)
    print(f"Generated Random Number: {random_number}")
    return {"random_number": random_number}

# Define the Lambda handler
lambda_handler = Mangum(app)
