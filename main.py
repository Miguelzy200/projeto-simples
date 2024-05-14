import asyncio

async def print1():
    print("en: Hello World!")

async def print2():
    print("pt-br: Olá Mundo!")

async def main():
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())

    await task1
    await task2

asyncio.run(main())