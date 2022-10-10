#Artur-Mihk Peterson
#10.10.22
#harjutame kilpkonna
import turtle

#tekitame akna
aken = turtle.Screen()
aken.setup(1000,1000)
turtle.speed(15)
aken.title("Kordamine 16- MM")


k1 = turtle.Turtle()
for i in range(5):
    for i in range(3):
        k1.color("green")
        k1.fd(50)
        k1.lt(120)

    k1.rt(90)
    for i in range(2):
        k1.color("black")
        k1.fd(60)
        k1.lt(90)
        k1.fd(50)
        k1.lt(90)

    k1.penup()
    k1.fd(60)
    k1.lt(90)
    k1.fd(15)
    k1.pendown()
    k1.lt(90)
    for i in range(3):
        k1.color("red")
        k1.fd(20)
        k1.rt(90)

    k1.penup()
    k1.right(180)
    k1.fd(40)
    k1.lt(90)
    k1.fd(60)
    k1.rt(90)
    k1.pendown()
#kilpkonn kaob   
k1.up()
k1.ht()
k1.goto(0, 0)
#kilpkonn tekib
k1.rt(90)
k1.fd(200)
k1.st()
k1.down()
k1.lt(90)

for i in range(5):
    for i in range(3):
        k1.color("green")
        k1.fd(50)
        k1.lt(120)

    k1.rt(90)
    for i in range(2):
        k1.color("black")
        k1.fd(60)
        k1.lt(90)
        k1.fd(50)
        k1.lt(90)

    k1.penup()
    k1.fd(60)
    k1.lt(90)
    k1.fd(15)
    k1.pendown()
    k1.lt(90)
    for i in range(2):
        k1.color("blue")
        k1.fd(20)
        k1.rt(90)
        
       

    k1.penup()
    k1.right(180)
    k1.fd(40)
    k1.lt(90)
    k1.fd(60)
    k1.rt(90)
    k1.pendown()


#suleb akna klickides
turtle.exitonclick()