def cal_area(radius):
    global area     #전역변수
    area=3.14*radius**2
    return

area=0
r=float(input("원의 반지름: "))
cal_area(r)
print(area)

def greet(name,msg="별일 없죠?"):
    print("안녕",name+','+msg)

greet("영희")

def calc(x,y,z):
    return x+y+z

print(calc(y=20,x=10,z=30)) #키워드 인수