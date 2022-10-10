#Artur-Mihk Peterson
#10.10.22
#harjutame kilpkonna
import turtle

#tekitame akna
aken = turtle.Screen()
aken.setup(300,300)
turtle.speed(5)
aken.title("ülesanne 1- MM")

#kllpkonna loomine
k1 = turtle.Turtle()
k2 = turtle.Turtle()
k3 = turtle.Turtle()
k4 = turtle.Turtle()
k5 = turtle.Turtle()
k6 = turtle.Turtle()
k7 = turtle.Turtle()
k8 = turtle.Turtle()

#värvide seadistamine
k1.color("red")
k2.color("cyan")
k3.color("blue")
k4.color("magenta")
k5.color("yellow")
k6.color("seagreen")
k7.color("aquamarine")
k8.color("navy")
#kilpkonna liigutamine
k1.lt(0)
k1.fd(100)
k2.lt(45)
k2.fd(100)
k3.lt(90)
k3.fd(100)
k4.lt(135)
k4.fd(100)
k5.lt(180)
k5.fd(100)
k6.lt(225)
k6.fd(100)
k7.lt(270)
k7.fd(100)
k8.lt(315)
k8.fd(100)


turtle.exitonclick()



