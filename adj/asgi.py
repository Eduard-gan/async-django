"""
ASGI config for adj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from asyncio import get_event_loop
from aio_pika import connect_robust
from adj import settings
from adj.consumers import consumer

async def kek():
    print("STA")
    from aiohttp import ClientSession
    async with ClientSession() as session:
        async with session.get("https://google.com") as resp:
            print(resp.status)
            print(await resp.text())

    connection = await connect_robust(f"amqp://{settings.RABBIT_USER}:{settings.RABBIT_PASSWORD}@{settings.RABBIT_IP}:5672/")
    settings.RABBIT_CHANNEL = await connection.channel()
    queue = await settings.RABBIT_CHANNEL.declare_queue(settings.RABBIT_QUEUE, durable=True)

    await queue.consume(consumer)


loop = get_event_loop()
loop.create_task(kek())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adj.settings')

application = get_asgi_application()
