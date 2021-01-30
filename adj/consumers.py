async def consumer(message):
    print(f"GOT MESSAGE: {message.body.decode()}")
    message.ack()
