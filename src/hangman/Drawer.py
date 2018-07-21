# import src.hangman.Word

import turtle as t

class Drawer:

    def game_screen(self):
        wn = t.Screen()
        t.hideturtle()

        self.game_intro()
        self.draw_base1()
        self.draw_base2()
        self.draw_base3()
        self.draw_base4()
        self.draw_circle()
        self.draw_body()
        self.draw_rightarm()
        self.draw_leftarm()
        self.draw_rightleg()
        self.draw_leftleg()

        t.exitonclick()

    def game_intro(self):
        t.penup()
        t.goto(-200, 300)
        t.write("Let's play some Hangman!", font=("Calibri", 24, "bold"))

    def draw_base1(self):
        t.goto(-250,-350)
        t.pendown()
        t.begin_fill()
        t.forward(450)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(450)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.end_fill()
        t.penup()

    def draw_base2(self):
        t.pendown()
        t.begin_fill()
        t.left(90)
        t.forward(550)
        t.right(90)
        t.forward(5)
        t.right(90)
        t.forward(550)
        t.end_fill()
        t.penup()
        t.goto(-250, 200)
        t.left(90)

    def draw_base3(self):
        t.pendown()
        t.forward(230)
        t.penup()

    def draw_base4(self):
        t.pendown()
        t.right(90)
        t.forward(100)
        t.penup()
        t.left(90)

    def draw_circle(self):
        t.goto(-20,0)
        t.pendown()
        t.circle(50)
        t.penup()

    def draw_body(self):
        t.pendown()
        t.right(90)
        t.forward(200)
        t.penup()

    def draw_rightarm(self):
        t.backward(200)
        t.pendown()
        t.left(55)
        t.forward(150)
        t.penup()

    def draw_leftarm(self):
        t.backward(150)
        t.pendown()
        t.right(110)
        t.forward(150)
        t.penup()

    def draw_rightleg(self):
        t.backward(150)
        t.left(55)
        t.forward(200)
        t.pendown()
        t.left(45)
        t.forward(150)
        t.penup()

    def draw_leftleg(self):
        t.backward(150)
        t.right(90)
        t.pendown()
        t.forward(150)
        t.penup()


