import random
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Change this number as needed
MAX_RANDOM_NUMBER = 100

@app.get("/")
def get_random_number():
    random_number = random.randint(0, MAX_RANDOM_NUMBER)
    print(f"Generated Random Number: {random_number}")
    return {"random_number": random_number}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
