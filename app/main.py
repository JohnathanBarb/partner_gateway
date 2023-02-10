from fastapi import FastAPI

from .partners import partner_router


app = FastAPI()

app.include_router(partner_router)


@app.get("/", tags=["Welcome"])
def root():
    return {"message": "Welcome to Partner Gateway"}
