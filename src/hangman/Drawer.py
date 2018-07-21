# import src.hangman.Word

import turtle as t

class Drawer:

    def game_screen(self):
        wn = t.Screen()

        self.game_intro()
        self.draw_circle()
        self.draw_body()
        self.draw_rightarm()
        self.draw_leftarm()

        t.exitonclick()

    def game_intro(self):
        t.penup()
        t.goto(-200, 300)
        t.write("Let's play some Hangman!", font=("Calibri", 24, "bold"))

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


