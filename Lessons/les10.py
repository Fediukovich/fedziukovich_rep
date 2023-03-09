# # from queue import Queue
# # from threading import Thread, current_thread, Lock, Semaphore, Barrier, Event
# # from time import sleep
# #
# #
# # lock1 = Lock()
# # q = Queue()
# # q.empty()
# # s = Semaphore(value=5)
# # b = Barrier(5)
# # e = Event()
# # # def main():
# # #     for _ in range(10):
# # #         lock1.acquire()
# # #         print(current_thread().name)
# # #         lock1.release()
# # #         sleep(1)
# #
# # # def main(i=None):
# # #     if i:
# # #         print(i)
# # #         for _ in range(10):
# # #             q.put(item=i)
# # #     else:
# # #         item = q.get()
# # #         print(item)
# #
# #
# # def main():
# #     print(current_thread().name)
# #     print(e.is_set())
# #     sleep(3)
# #     e.set()
# #
# #
# # def bar():
# #     e.wait()
# #     print(e.is_set())
# #     print(current_thread().name)
# #
# #
# # if __name__ == '__main__':
# #     # threads = [Thread(target=main, name=f'Thread-{i}', args=('queue', ) if i == 1 else ()) for i in range(1, 11)]
# #     threads = [Thread(target=main), Thread(target=bar)]
# #     for thread in threads:
# #         thread.start()
# # from multiprocessing import Process, Semaphore, Barrier, Lock, Queue, Pipe, current_process
# # from time import sleep
# #
# # lock = Lock()
# #
# #
# # def main():
# #     for _ in range(10):
# #         lock.acquire()
# #         print(current_process().name)
# #         lock.release()
# #         sleep(1)
# #
# #
# # if __name__ == '__main__':
# #     processes = [Process(target=main, name=f'Process-{_}') for _ in range(10)]
# #     for process in processes:
# #         process.start()
# from asyncio import sleep
# import aiofiles
# import asyncio
#
#
# async def foo(i):
#     for _ in range(10):
#         print(i)
#         await sleep(1)
#
#
# async def main():
#     async with aiofiles.open('input.json', 'r', encoding='utf-8') as file:
#         data = await file.read()
#     tasks = [asyncio.create_task(foo(i)) for i in range(10)]
#     for task in tasks:
#         await task
#
#
# if __name__ == '__main__':
#     # asyncio.set_event_loop(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(main())
# from threading import Thread
#
# from requests import Session
#
#
# def get_currency(cur_id: int):
#     with Session() as session:
#         response = session.get(
#             url=f'https://www.nbrb.by/api/exrates/currencies/{cur_id}/',
#         )
#         print(response.status_code)
#
#
# if __name__ == '__main__':
#     threads = [Thread(target=get_currency, args=(431, )) for _ in range(100)]
#     for thread in threads:
#         thread.start()


from aiohttp import ClientSession
import asyncio


async def get_currency(cur_id: int):
    async with ClientSession(base_url='https://www.nbrb.by') as session:
        async with session.get(
            url=f'/api/exrates/currencies/{cur_id}/',
        ) as response:
            print(response.status)


async def main():
    tasks = [asyncio.create_task(get_currency(431)) for _ in range(100)]
    for task in tasks:
        await task


if __name__ == '__main__':
    asyncio.run(main())
