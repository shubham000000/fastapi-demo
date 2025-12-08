from fastapi import FastAPI

# Initialize the app
app = FastAPI()

# Basic home endpoint
@app.get("/")
def home():
    return {"message": "Hello Shubham, your FastAPI service is live!"}

# A parameterized endpoint
@app.get("/square/{num}")
def square_number(num: int):
    return {"number": num, "square": num * num}

# A POST endpoint example
@app.post("/greet")
def greet_user(payload: dict):
    name = payload.get("name", "Guest")
    return {"greeting": f"Welcome aboard, {name}!"}
