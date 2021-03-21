def binarySearch(alist, item):
        if len(alist) == 0:
            return False
        else:
            midpoint = len(alist)//2
            if alist[midpoint]==item:
              return True
            else:
              if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
              else:
                return binarySearch(alist[midpoint+1:],item)
testlist=[]
for i in range(9):
    x=eval(input())
    testlist.append(x)
print("请输入要查找的数!")
item=eval(input())
print(binarySearch(testlist, item))
