a=int(input("정수를 입력하시오 : "))
b=int(input("정스를 입력하시오 : "))
if(a>b):
    print(a,"를 ",b,"로 나눈 몫=",a//b,", 나머지=",a%b)
else:
    print(b, "를 ", a, "로 나눈 몫=",b // a, ", 나머지=", b % a)