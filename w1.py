import time
f = open('c:/test1/test1.txt','a+')
t1=time.ctime()
text=': Montri'
f.write(t1+text+'\n')
data=f.read()
print(data)
f.close()