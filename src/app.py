from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Welcome"])
def root():
    return {"message": "Welcome to Partner Gateway"}
