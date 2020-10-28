import asyncio


async def hello(inputs):
    print(f'{asyncio.Task.current_task()}')
    print(f'{asyncio.get_running_loop()}')
    print('hello world')
    print(inputs)

if __name__ == '__main__':
    data = "Asyncio Program"
    asyncio.run(hello(data))