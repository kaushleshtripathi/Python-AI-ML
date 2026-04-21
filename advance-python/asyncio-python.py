import asyncio 

def one():
    print("one")

async def two():
    print("two")
    await asyncio.sleep(3)
    print("two finished") 


async def three():
    print("three")
    await asyncio.sleep(1)
    print("three finished")      


def four():
    print("four")


async def main():
    one()
    task1 = asyncio.create_task(two())
    task2 = asyncio.create_task(three())
    four()

    await task1
    await task2 


asyncio.run(main())