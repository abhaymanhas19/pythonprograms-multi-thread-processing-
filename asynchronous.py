import asyncio
import time
import threading
import os
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import requests
# To avoid deprecation warning at runtime .
# import warnings
# warnings.filterwarnings("ignore",category=DeprecationWarning)


img_urls=[
    "https://images.pexels.com/photos/16791436/pexels-photo-16791436/free-photo-of-no-idea-3.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load",
    "https://images.pexels.com/photos/16884192/pexels-photo-16884192/free-photo-of-lady-in-red.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
]


async def main(url):
        img=requests.get(url=url).content
        print("Downloading")
        await img
# async def fun1(i):
#     print(os.getpid(), threading.current_thread().name)
#     return i*i
  
# def main(n):
#     return asyncio.run(fun1(n))

async def multi():
    with multiprocessing.Pool() as p:
        result=p.map(main,img_urls)
        # await result
    print(result)
    

if __name__=="__main__":
    start_time=time.perf_counter()
    asyncio.run(multi())
    end_time=time.perf_counter()

    print(end_time-start_time)
   
























# async def fun1():
#     print("start intaislzw 1")
#     await asyncio.sleep(2)
#     await asyncio.create_task(fun2())
#     print("done 1")

# async def fun2():
#     print("start intaislzwv 2")
#     await asyncio.sleep(4)
#     print("done 2")

# asyncio.run(fun1())
    # task=asyncio.create_task(fun1())
    # task2=asyncio.create_task(fun2())
    # await task
    # await task2
    # await  asyncio.gather(fun1(),fun2())
#    print(result)


# loop=asyncio.get_event_loop()
# loop.run_until_complete(fun1())
# loop.close()
# asyncio.run(main())




# class ProcessApi:
#     def get_task(self,session,jobs):
#         tasks=[]
#         for job in jobs:
#             tasks.append(session.post(url='https://api.openai.com/v1/chat/completions',headers=request_header,json=job))
#         return tasks

#     async def _get_request(self,jobs):
#         results=[]
#         async with aiohttp.ClientSession() as session:
#             tasks=self.get_task(session,jobs)
#             response=await asyncio.gather(*tasks)
#             for i in response:
#                 results.append(await i.json())
#             return results
