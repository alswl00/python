from random import randint

x=randint(0,2);win=""

while True:
    print("*****가위바위보게임*****")
    print("다음 중 하나를 선택하세요.")
    num=int(input("가위(0), 바위(1), 보(2), 종료(3) : "))
    if(num==3) :break;
    if(x==num) :win="비겼습니다."
    if(x==0):
        com="가위"
        if(num==1):win="이겼습니다."
        elif(num==2):win="졌습니다."
    elif(x==1) :
        com="바위"
        if(num==0):win="졌습니다."
        elif(num==2):win="이겼습니다."
    elif(x==2) :
        com="보"
        if(num==0):win="이겼습니다."
        elif(num==1) : win="졌습니다."
    print("컴퓨터는 ",com,"를 냈습니다.")
    print(win)
