import random
cnt=[0,0,0,0,0,0]
for i in range(1000):
    value=random.randint(0,5)
    cnt[value]=cnt[value]+1
for i in range(6):
    print("주사위가",i+1,"인 경우는 ",cnt[i],"번")