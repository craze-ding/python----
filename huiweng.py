x=input("请输入一个多位数!\n")
flag = True 
for i in range(len(x)//2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print (x+"是一个回文数!")
else:
    print (x+"不是一个回文数!")
"""
x=input("请输入一个多位数!\n")
str_x = x
if str_x == str_x[::-1]:
    print (x+"是一个回文数!")
else:
    print (x+"不是一个回文数!")
"""