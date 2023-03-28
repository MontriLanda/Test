# multiprocessing programming
import time
import multiprocessing

def x2(x):
    return x*2
# Cerate function multi processing
def multiprocessing_func(x):
    y=x*x
    time.sleep(1)
    print('{} * = {}'.format(x,x2(y)))
if __name__=='__main__':
    starttime = time.time()
    
    process=[]
    cpu_cores=multiprocessing.cpu_count()
    
    for i in range(0,cpu_cores):
        p=multiprocessing.Process(target=multiprocessing_func,args=(i,))
        process.append(p)
        p.start()
        
    for process in process:
        process.join()
        
    print('time :: {} Seconds'.format(time.time()-starttime))