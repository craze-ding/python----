import time as t
t1=t.time()
a,b=eval(input("请输入两个数!\n"))
def yanZi(x):
    ls=[]
    for i in range(1,x+1):
        if x%i==0:
            ls.append(i)
    return ls
def MAX(a,b):
    maxD=1
    for i in range(len(a)):
        for n in range(len(b)):
            if a[i]==b[n]:
                maxD=a[i]
    return maxD
list_a=yanZi(a)
list_b=yanZi(b)
maxD=MAX(list_a,list_b)
print(maxD)
t2=t.time()
print(t2-t1)
"""
#使用辗转相除法求最大公约数
a,b=eval(input())
def gcd(a,b):
    # a作为除数 必须大于b
    a, b = (a, b) if a >=b else (b, a)
    while b:
        a,b = b,a%b
    return a
maxD=gcd(a,b)
print(maxD)
"""