import numpy as np
t1 = np.array([1,2,3])
print(t1.shape,t1)
print(t1)

t2=np.arange(1,25)
t3=t2.reshape(4,6)
print(t3,t3.shape)

t4=t2.reshape(2,6,2)
print(t4,t4.shape)
#获取连续的行和列,半开半闭区间
t5 = t3[0:3,1:4]
print(t5)
print(t3[[0,2],:])
print(t3)
t3[1,1]=20
print(t3[t3>10])
