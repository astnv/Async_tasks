import asyncio

# Общая переменная
counter = 0

async def increment():
    global counter
    for _ in range(1000):
        counter += 1  # Увеличиваем счетчик

async def main():
    # Запускаем две корутины одновременно
    await asyncio.gather(increment(), increment())

# Запускаем основную функцию
asyncio.run(main())
print(counter) 