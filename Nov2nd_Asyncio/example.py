import asyncio
import time

async def add(a, b):
   c = a + b
   return c
   
async def sub(a, b):
   c = a - b
   return c
   
async def range_of_num():
    for i in range(0, 10000, 5):
    #    if i == 2000:
    #       await asyncio.sleep(10)
        print(i, end=" ")
   
async def main():

    task3 = loop.create_task(range_of_num())
	await asyncio.sleep(0.1)
    task1 = loop.create_task(add(4, 5))
    task2 = loop.create_task(sub(6, 2))
    await task1
    await task2
    await task3
    return task1, task2, task3

if __name__ == "__main__":
    print(f"started time : {time.strftime('%X')}")
    loop = asyncio.get_event_loop()
    r1, r2, r3 = loop.run_until_complete(main())
    print(f"{r1.result()}")
    print(f"{r2.result()}")
    print(f"{r3.result()}")
    loop.close()
    print(f"End time : {time.strftime('%X')}")
