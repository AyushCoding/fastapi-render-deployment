from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI deployed successfully"}


@app.get("/users")
def get_users():
    return {"users": ["John", "Alice"]}