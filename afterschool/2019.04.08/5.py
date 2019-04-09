import turtle
t = turtle.Turtle()
t.shape("turtle")

#리스트를 사용하여 색상을 문자열로 저장한다
color_list=["yellow","red","blue","green"]
j=0
for i in range(4):
    t.forward(j+i*20)
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()

turtle.exitonclick()