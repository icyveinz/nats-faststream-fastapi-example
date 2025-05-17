import os
from fastapi import FastAPI
from faststream.rabbit import RabbitBroker

app = FastAPI()

BROKER_URL = os.getenv("BROKER_URL", "amqp://guest:guest@localhost:5672/")
broker = RabbitBroker(BROKER_URL)

@app.on_event("startup")
async def startup():
    await broker.connect()

@app.on_event("shutdown")
async def shutdown():
    await broker.close()

@app.post("/publish")
async def publish(data: dict):
    await broker.publish(data, queue="events")
    return {"message": "Published successfully"}

