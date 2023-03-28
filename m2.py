import multiprocessing
import time


def x2(x):
    return x*2
cpu_core = multiprocessing.cpu_count()
starttime=time.time()
for i in range (0,cpu_core):
    y=i*i
    # time.sleep(1)
    print('{}*2 = {}'.format(i,x2(y)))
print('time :: {} Seconds'.format(time.time()-starttime))