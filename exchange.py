while 1:
    suShu=eval(input("请输入大于2的一个数\n"))
    loGO=1
    for i in range(2,suShu):
        if suShu%i==0:
            loGO=0
            break         
    if loGO==0:
        print("这不是一个素数!")
    else:
        print("这是一个素数!")
"""
import time
t1=time.time()
l = []
for x in range(100):
    #判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x <2:
        continue
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        l.append(x)
print(l) #  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
t2=time.time()
print(t2-t1)

import math
import time  
lst = []
count1 = 0
count2 = 0
t1=time.time()
for i in range(3,10000000,2):    
    j = math.sqrt(i)    
    j = math.ceil(j)    
    for x in range(3,j+1,2):    
        count1 += 1
        if i % x == 0:
            count2 += 1
            break
    else:
        lst.append(i)        
else:  
    print(count1,count2)
    print([2] + lst)
    t2=time.time()
    print(t2-t1)
"""
