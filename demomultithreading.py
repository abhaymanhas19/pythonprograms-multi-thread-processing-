import time
import multiprocessing
import os 
import threading
import requests
from pathos.multiprocessing import ProcessPool
from concurrent.futures import ThreadPoolExecutor


img_urls=[
    "https://images.pexels.com/photos/16791436/pexels-photo-16791436/free-photo-of-no-idea-3.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load",
    "https://images.pexels.com/photos/16884192/pexels-photo-16884192/free-photo-of-lady-in-red.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
]


def main(url):
    img=requests.get(url=url).content
    print("Downloading")
    return img


# def normal_function():
#     print("ID of process running function1: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16791436/pexels-photo-16791436/free-photo-of-no-idea-3.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load"
    # response=requests.get(url=url)
    # with open("images/images.jpg","wb") as image:
    #     image.write(response.content)

    # print("Image one download ")

# def normal_function2():
#     print("ID of process running funtion2: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16884192/pexels-photo-16884192/free-photo-of-lady-in-red.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images2.jpg","wb") as image:
    #     image.write(response.content)

    # print("Image second download ")

# def normal_function3():
#     print("ID of process running funtion3: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images1.jpg","wb") as image:
    #     image.write(response.content)
    # print("Image third download ")

# def normal_function4():
#     print("ID of process running funtion4: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images1.jpg","wb") as image:
    #     image.write(response.content)
    # print("Image third download ")

# def normal_function5():
#     print("ID of process running funtion4: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images1.jpg","wb") as image:
    #     image.write(response.content)
    # print("Image third download ")

# def normal_function6():
#     print("ID of process running funtion4: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images1.jpg","wb") as image:
    #     image.write(response.content)
    # print("Image third download ")

# def normal_function7():
#     print("ID of process running funtion4: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images1.jpg","wb") as image:
    #     image.write(response.content)
    # print("Image third download ")

# def normal_function8():
#     print("ID of process running funtion4: {}".format(os.getpid()))
    # url="https://images.pexels.com/photos/16248187/pexels-photo-16248187/free-photo-of-jetty-light-sea-dawn.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    # response=requests.get(url=url)
    # with open("images/images1.jpg","wb") as image:
    #     image.write(response.content)
    # print("Image third download ")

if __name__ == "__main__":
    # start_time = time.time()
    # normal_function()
    # normal_function2()
    # normal_function3()
    # end_time = time.time()
    # elapsed_time_normal = end_time - start_time
    # print("Elapsed time for normal function:", elapsed_time_normal, "seconds")

    start_time = time.perf_counter()
    for i in img_urls:
        main(i)
    end_time = time.perf_counter()
    

    elapsed_time_multiprocessing = end_time - start_time
    print("Elapsed time for normal function:", elapsed_time_multiprocessing, "seconds")


    #-------------------------------------------------------------------------- Threading 
    # start_time = time.perf_counter()
    # l=[]
    # for i in img_urls:
    #    t=threading.Thread(target=main,args=(i,))
    #    l.append(t)
    # for i in l:
    #     i.start()
    # for i in l:
    #     i.join()
    # end_time = time.perf_counter()

    start_time = time.perf_counter()
    with ThreadPoolExecutor() as p:
       p.map(main,img_urls)
    end_time = time.perf_counter()


    elapsed_time_multiprocessing = end_time - start_time
    print("Elapsed time for threading function:", elapsed_time_multiprocessing, "seconds")


#--------------------------------------------------------------Multiprocessing





    # start_time = time.perf_counter()
    # l=[]
    # for i in img_urls:
    #    t=multiprocessing.Process(target=main,args=(i,))
    #    l.append(t)
    # for i in l:
    #     i.start()
    # for i in l:
    #     i.join()
    # end_time = time.perf_counter()

    start_time = time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(main,img_urls)
    end_time = time.perf_counter()

    
 
    # t1=multiprocessing.Process(target=normal_function)
    # t2=multiprocessing.Process(target=normal_function2)
    # t3=multiprocessing.Process(target=normal_function3)
    # t4=multiprocessing.Process(target=normal_function4)
    # t5=multiprocessing.Process(target=normal_function5)
    # t6=multiprocessing.Process(target=normal_function6)
    # t7=multiprocessing.Process(target=normal_function7)
    # t8=multiprocessing.Process(target=normal_function8)




  
    # list_of_func=[normal_function,normal_function2,normal_function3,normal_function4,normal_function5,normal_function6,normal_function7,normal_function8]
#    with multiprocessing.Pool() as f:
#         f.map(lambda f: f(), list_of_func)
    # with ProcessPool() as f:
    #     f.map(lambda f: f(), list_of_func)
  
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # t7.start()
    # t8.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()


    elapsed_time_multiprocessing = end_time - start_time
    print("Elapsed time for multiprocessing function:", elapsed_time_multiprocessing, "seconds")
