from potoki import posled, potok
from proc import kvadrat
from asinxron import async_tasks, sync_tasks
import asyncio

async def main():
    first_1 = posled()
    first_2 = potok()
    second = kvadrat()
    third_1 = await async_tasks()
    third_2 = sync_tasks()
    
if __name__ == "__main__":
    asyncio.run(main()) 

