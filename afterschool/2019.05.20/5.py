def happyBirthday(name):
    for i in range(4):
        print("Happy Birthday",end="")
        if i==2: print(", dear",name)
        else:print(" to you!")
    return;

name=input("이름을 입력하세요>>")
happyBirthday(name)