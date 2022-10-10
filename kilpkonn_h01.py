#Artur-Mihk Peterson
#10.10.22
#harjutame kilpkonna
import turtle

#tekitame akna
aken = turtle.Screen()
aken.setup(300,300)
turtle.speed(10)
aken.title("Kordamine 1- MM")


k1 = turtle.Turtle()

for i in range(4):
    k1.fd(30)
    k1.rt(90)
    k1.fd(30)
    k1.lt(90)
    k1.fd(30)
    k1.lt(90)
    
#suleb akna klickides
turtle.exitonclick()