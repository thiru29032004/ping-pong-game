import turtle
import winsound

win=turtle.Screen()
win.setup(800,600)
win.bgcolor("black")
win.title("Pong game")
win.tracer(0)
#ball
ball=turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.speed(-1)
ball.dx=0.5
ball.dy=0.5


#line and round making
line=turtle.Turtle()
line.goto(-400,-300)
line.speed(0)
line.color("white")
line.hideturtle()
line.forward(800)
line.left(90)
line.forward(600)
line.left(90)
line.forward(800)
line.left(90)
line.forward(600)
line.left(90)

cline=turtle.Turtle()
x=(0,300)
y=(0,-300)
cline.color("white")
cline.hideturtle()
cline.penup()
cline.goto(x)
cline.pendown()
cline.goto(y)

Circle = turtle.Turtle()
Circle.color("white")
Circle.hideturtle()
Circle.goto(0,-50)
Circle.circle(50)
#pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.goto(0,260)
pen.hideturtle()
pen.clear()
#score
score_a=0
score_b=0
pen.write(f"Player A:{score_a}       Player B:{score_b}", align="center", font=("Arial", 14, "normal"))


#left and right paddle
left_paddle=turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.penup()
left_paddle.speed(0)
left_paddle.shapesize(stretch_len=1,stretch_wid=5)
left_paddle.goto(-350,0)

right_paddle=turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.penup()
right_paddle.speed(0)
right_paddle.shapesize(stretch_len=1,stretch_wid=5)
right_paddle.goto(350,0)

#paddle moment
def left_paddle_moveup():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_movedown():
    left_paddle.sety(left_paddle.ycor()-20)

def right_paddle_moveup():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_movedown():
    right_paddle.sety(right_paddle.ycor()-20)

#ball moment


win.listen()
win.onkeypress(left_paddle_moveup,"w")
win.onkeypress(left_paddle_movedown,"s")
win.onkeypress(right_paddle_moveup,"Up")
win.onkeypress(right_paddle_movedown,"Down")




while True:

    win.update()
    ball.sety(ball.ycor() +ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #after hitting
    #print("Ball Position:", ball.xcor(), ball.ycor())
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1


    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy*=-1
    #
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write(f"Player A:{score_a}       Player B:{score_b}", align="center", font=("Arial", 14, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx*=-1
        score_b += 1
        pen.clear()
        pen.write(f"Player A:{score_a}       Player B:{score_b}", align="center", font=("Arial", 14, "normal"))

    #paddle and ball collision
    #print("Left Paddle Position:", left_paddle.xcor(), left_paddle.ycor())
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.speed(0)
        wav_path = "sounds/Pong_bounce.wav"
        winsound.PlaySound(wav_path, winsound.SND_FILENAME)




    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < left_paddle.ycor()+50 and ball.ycor() > left_paddle.ycor() -50:
        ball.setx(-340)
        ball.dx*=-1
        ball.speed(0)
        wav_path = "sounds/Pong_bounce.wav"
        winsound.PlaySound(wav_path, winsound.SND_FILENAME)






