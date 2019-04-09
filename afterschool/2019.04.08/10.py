year=int(input("연도를 입력하시오: "))
if year%4==0 and not(year%100==0) or year%400==0:
    print(year,"은 윤년입니다.")