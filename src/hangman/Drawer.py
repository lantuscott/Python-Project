# import src.hangman.Word

import turtle as t

class Drawer:

    def game_screen(self):
        wn = t.Screen()
        t.speed("fastest") # Fastest speed
        t.hideturtle()

        self.game_intro()

    def game_intro(self):
        t.penup()
        t.goto(-200, 300)
        t.write("Let's play some Hangman!", font=("Calibri", 24, "bold"))

    def draw_base1(self):
        t.goto(-250, -350)
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

    def draw_face(self):
        t.goto(-20, 0)
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

    def game_over(self):
        t.goto(-150, -50)
        t.pencolor("red")
        t.write("Game Over!", font=("Calibri", 40, "bold"))

    def method_factory(self, methodNumber):
        if methodNumber == 0:
            self.draw_base1()
        elif methodNumber == 1:
            self.draw_base2()
        elif methodNumber == 2:
            self.draw_base3()
        elif methodNumber == 3:
            self.draw_base4()
        elif methodNumber == 4:
            self.draw_face()
        elif methodNumber == 5:
            self.draw_body()
        elif methodNumber == 6:
            self.draw_rightarm()
        elif methodNumber == 7:
            self.draw_leftarm()
        elif methodNumber == 8:
            self.draw_rightleg()
        elif methodNumber == 9:
            self.draw_leftleg()
            self.game_over()
            t.exitonclick()
