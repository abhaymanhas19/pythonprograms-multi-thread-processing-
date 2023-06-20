import threading
import time
import multiprocessing
import os
from pathos.multiprocessing import ProcessPool
import asyncio
from concurrent.futures import ThreadPoolExecutor



def fun1():
    print("ID of process running fun1: {}".format(os.getpid()),threading.current_thread().name)

    # start_time=time.time()  
    # l=[]
    # for i in range(10):
    #     l.append(i*i)
    # end_time=time.time() 
    # # print(" THe time taken by function one is ",end_time-start_time)
    # return l


def fun2():
    print("ID of process running fun2: {}".format(os.getpid()),threading.current_thread().name)

    # l=[]
    # start_time=time.time()  
    # for i in range(1000):
    #     l.append(i+2)
    # end_time=time.time() 
    # # print(" THe time taken by function SECOND is ",end_time-start_time)
    # return l

def fun3():
    print("ID of process running fun3: {}".format(os.getpid()),threading.current_thread().name)
  
    # l=[]
    # start_time=time.time()
    # for i in range(1000):
    #     l.append(i+i)
    # end_time=time.time() 
    # # print(" THe time taken by function tHIRD is ",end_time-start_time)
    # return l
def fun4():
    print("ID of process running fun4: {}".format(os.getpid()),threading.current_thread().name)
    # l=[]
    # start_time=time.time()
    # for i in range(1000):
    #     l.append(i+i)
    # end_time=time.time() 
    # # print(" THe time taken by function tHIRD is ",end_time-start_time)
    # return l
def fun5():
    print("ID of process running fun5: {}".format(os.getpid()),threading.current_thread().name)
    # l=[]
    # start_time=time.time()
    # for i in range(1000):
    #     l.append(i+i)
    # end_time=time.time() 
    # # print(" THe time taken by function tHIRD is ",end_time-start_time)
    # return l

if __name__=="__main__":
    # function_time=time.time()
    # fun1()
    # print("1")
    # fun2()
    # print("2")
    # fun3()
    # print("3")
    # fucntion_end_time=time.time()
    # print(f"Three function take {fucntion_end_time - function_time} time to complete it,s execuation.")

#-----------------------------------------------------Threading


   # p=[]
    # for  i in list_of_func:
    #     process=threading.Thread(target=fun1)
    #     p.append(process)   
    # for process in p:
    #     process.start()
    # for process in p:
    #     process.join()
   
    list_of_func = [fun1, fun2, fun3, fun4,fun5]
    # with ThreadPoolExecutor(2) as t:
    #     t.map(lambda f: f(), list_of_func)
  

    # t1=threading.Thread(target=fun1)
    # t2=threading.Thread(target=fun2)
    # t3=threading.Thread(target=fun3)
    # t4=threading.Thread(target=fun4)
    # t5=threading.Thread(target=fun5)







#------------------------------------Multiprocessing


    # lock=multiprocessing.Lock()
    # lock=multiprocessing.RLock()
    # lock=multiprocessing.Semaphore()
 

  
    # start_time=time.time()

    # with multiprocessing.Pool(processes=3) as f:
    #     f.map(lambda f: f(), list_of_func)
    with ProcessPool(nodes=3) as pool:
        pool.map(lambda f: f(), list_of_func)


    # t1=multiprocessing.Process(target=fun1)
    # t2=multiprocessing.Process(target=fun2)
    # t3=multiprocessing.Process(target=fun3)
    # t4=multiprocessing.Process(target=fun4)
    # t5=multiprocessing.Process(target=fun5)


    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()

    # p=[]
    # for  i in list_of_func:
    #     process=multiprocessing.Process(target=fun1)
    #     p.append(process)   
    # for process in p:
    #     process.start()
    # for process in p:
    #     process.join()
    
    # # end_time=time.time()
    # print(f"Three function take {round((end_time-start_time),2)} time to complete it,s execuation by using multi-threading or multiprocessing.")
    