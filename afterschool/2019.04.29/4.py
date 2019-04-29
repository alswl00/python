sum=0
n=int(input("정수를 입력하시오:"))
for i in range(1,n,1):
    sum+=i
print("1~",n,"까지 합=",sum)

fact=1
n=int(input("정수를 입력하시오:"))
for i in range(1,n+1):
    fact*=i
print(n,"! =",fact)