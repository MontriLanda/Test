import time
import multiprocessing as mp

starttime=time.time()
def job(a,x):
    for i in range(500000):
        x+=1
        # time.sleep(1)
        print('%s=%d'%(a,x))
if(__name__=='__main__'):
    p1=mp.Process(target=job,args=('x',1))
    p2=mp.Process(target=job,args=('y',11))
    p1.start()
    p2.start()
    print("สั่งงานให้เครื่องทำงานแล้ว")
    print('time :: {} Seconds'.format(time.time()-starttime))