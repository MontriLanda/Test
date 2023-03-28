import multiprocessing as mp
import time

starttime=time.time()
def job():
    for i in range(100000):
        2**2
    print("งานเสร็จแล้ว")
if(__name__=='__main__'):
    p=mp.Process(target=job)
    p.start()
    print("สั่งงาน")
print('time :: {} Seconds'.format(time.time()-starttime))