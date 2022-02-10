#거북이가 선으로  도형 그리기(좌표이용)
import turtle as t
t.shape("turtle") 
t.color("blue")

for x in range(4):
    t.forward(100)
    t.left(90)
t.up()
t.goto(200,200)
t.down()
for x in range(5):
    t.forward(100)
    t.left(72)
t.up()
t.goto(-200,200)
t.down()
for x in range(6):
    t.forward(100)
    t.left(60)
t.up()
t.goto(200,-200)
t.down()
for x in range(5):
    t.forward(100)
    t.left(144)

    

