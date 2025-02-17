import asyncio

from faststream.nats import NatsBroker
import aiohttp
import os

NATS_URL = os.getenv("NATS_URL", "nats://nats:4222")

broker = NatsBroker(NATS_URL)

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