from fastapi import FastAPI
from routes import inventory

app=FastAPI() 

app.include_router(inventory.router)


@app.get("/")
async def root():
    return{"mas":"hello bro",}