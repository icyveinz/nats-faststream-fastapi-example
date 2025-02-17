from fastapi import FastAPI
from nats.aio.client import Client as NATS
import asyncio
import os

app = FastAPI()

NATS_URL = os.getenv("NATS_URL", "nats://localhost:4222")

async def publish_message(data: dict):
    nc = NATS()
    await nc.connect(NATS_URL)
    await nc.publish("events", str(data).encode())
    await nc.close()

@app.post("/publish")
async def publish(data: dict):
    asyncio.create_task(publish_message(data))
    return {"message": "Published successfully"}
