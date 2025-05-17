import os
import asyncio
import aiohttp
from faststream.rabbit import RabbitBroker

BROKER_URL = os.getenv("BROKER_URL", "amqp://guest:guest@rabbitmq:5672/")
broker = RabbitBroker(BROKER_URL)

@broker.subscriber("events")
async def process_message(message: dict):
    print(f"Received message: {message}")

    async with aiohttp.ClientSession() as session:
        async with session.post("http://example.com/process", json=message) as response:
            print(f"Response: {await response.text()}")

async def main():
    await broker.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
