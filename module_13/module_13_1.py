import asyncio


async def start_strongman(name: str, power: int) -> None:
    print(f'Силач {name} начал соревнования.')
    await_time = (5 / power) +1
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(await_time)
    print(f'Силач {name} закончил соревнование.')


async def start_tournament():
    print('Турнир начался.')
    # TODO Разобраться с выполнением задач в цикле
    """tasks = []
    for name, power in kwargs.items():
        print(name, power)
        tasks += await (start_strongman(name, power))
        #return tasks
        await asyncio.gather(*tasks)
    await tasks"""
    task1 = asyncio.create_task(start_strongman('Амбал', 10))
    task2 = asyncio.create_task(start_strongman('Стрелка', 3))
    task3 = asyncio.create_task(start_strongman('Барабанщик', 5))
    await asyncio.gather(task1, task2, task3)

if __name__ == '__main__':
    #players = {'Силач': 10, 'Стрелка': 5, 'Барабанщик': 3}
    asyncio.run(start_tournament())
