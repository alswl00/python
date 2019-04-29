n=int(input("원하는 단은:"))

for i in range(1,10):
    print("%s*%s=%s"%(n,i,n*i))
print()

num=1
while num<=9:
    print("%s*%s=%s"%(n,num,n*num))
    num+=1