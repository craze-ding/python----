def bubbleSort(ls):
    frist=0
    last=len(ls)
    exchanges = True
    while frist >= 0 and exchanges:
        exchanges = False
        i=frist
        for n in range(frist+1,last):
            if ls[i]>ls[n]:
                exchanges = True
                temp=ls[i]
                ls[i]=ls[n]
                ls[n]=temp
        frist=frist+1
    return ls       
def great():
    ls=[]
    for i in range(10):
        ls.append(eval(input()))
    return ls
ls=great()   
print(ls)
ls=bubbleSort(ls)
print(ls)