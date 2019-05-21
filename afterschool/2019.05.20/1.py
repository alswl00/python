num=0;
while True:
    print("손님 주문하시겠습니까 ?")
    num=int(input("<1>카페라떼 <2>카푸치노 <3>아메리카노 <4>그만시킬래요 ==>"))
    if(num==1) :menu="카페라떼"
    elif(num==2):menu="카푸치노"
    elif(num==3):menu="아메리카노"
    else:break;
    print(menu,"주문하셨습니다.")
