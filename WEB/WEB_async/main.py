import time
from random import randint
import asyncio
import os

ITER_NUM = 10
COROUT_NUM = 5


async def do_some_work(i):
    for j in range(ITER_NUM):
        print(f"{i * ' ' + chr(9608) + (COROUT_NUM - i) * ' '}"
              f"Работник {i} прогресс: {j} {chr(9632) * j}")
        await asyncio.sleep(0.01 * randint(1, 10))


async def main():
    task = []
    for i in range(COROUT_NUM):
        task.append(asyncio.create_task(do_some_work(i)))
    await asyncio.gather(*task)


if __name__ == "__main__":
    asyncio.run(main())
