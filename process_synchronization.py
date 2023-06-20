import multiprocessing



def Book_seat(seat,n,lock):
    lock.acquire()
    print(f"process {n} seat available {seat.value}")
    if seat.value>0:
        seat.value-=1
        print(f"Seat confirmed for process {n}")
    else:
        print("seat is full")
    lock.release()

seat=multiprocessing.Value("i",2)
lock=multiprocessing.Lock()

 #$sychronization in multiptrocessing 


#   lock=multiprocessing.Lock()   #apply a lock on shared resource thta is acquire by first process no one other process thta shared resouce until the previous one is release the lock.
#     lock=multiprocessing.RLock()   # same process or thread can acquire the lock 
#     lock=multiprocessing.Semaphore()  $ in which we can apply a condition how many process or threads  can acquire the lock at the single time or simultaneouly 



process1= multiprocessing.Process(target=Book_seat,args=(seat,1,lock))
process2= multiprocessing.Process(target=Book_seat,args=(seat,2,lock))
process3= multiprocessing.Process(target=Book_seat,args=(seat,3,lock))
process4= multiprocessing.Process(target=Book_seat,args=(seat,4,lock))


process1.start()
process2.start()
process3.start()
process4.start()
process1.join()
process2.join()
process3.join()
process4.join()
