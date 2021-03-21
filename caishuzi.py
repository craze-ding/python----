import random 
x=random.randint(0,100)
chance=eval(input("请输入一个数!\n")) 
print("共%d次机会" % (chance))
for i in range(1, chance + 1):
    y=eval(input("请输入一个数!\n"))    
    if y<x:
        print("小了!!!还剩%d次机会"%(chance-i))        
        continue
    elif y>x:
        print("大了!!!还剩%d次机会"%(chance-i))       
        continue
    else:
        print("恭喜你!猜对了!")
        exit(0)
    