import json
from fastapi import FastAPI
from nats.aio.client import Client as NATS
import asyncio
import os

app = FastAPI()

NATS_URL = os.getenv("NATS_URL", "nats://localhost:4222")

async def publish_message(data: dict):
    nc = NATS()
    await nc.connect(NATS_URL)
    # Use json.dumps to create a proper JSON string
    await nc.publish("events", json.dumps(data).encode("utf-8"))
    await nc.close()

@app.post("/publish")
async def publish(data: dict):
    asyncio.create_task(publish_message(data))
    return {"message": "Published successfully"}
