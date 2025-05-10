import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return "Result"

async def main():
    future = asyncio.Future()  # Создание объекта Future
    result = await my_coroutine()  # Ожидание результата корутины
    future.set_result(result)  # Установка результата в Future
    print(future.result())  # Получение результата из Future

asyncio.run(main())