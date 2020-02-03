#this is based on the code from FreeCodeCamp tutorial at https://www.youtube.com/watch?v=XGf2GcyHPhc&list=WL&index=11
#i'm adding to the code in order to practice and learn


import turtle as tn
import time
import winsound

game_speed = 0.02
score_a = 0
score_b = 0

wn = tn.Screen()
wn.title("Pong by @TiagoS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Objects - Paddles and Ball

paddle_a = tn.Turtle()
paddle_a.speed(0)
# 20 px by 20 px default
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-370,0)

paddle_b = tn.Turtle()
paddle_b.speed(0)
# 20 px by 20 px default
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(370,0)

ball = tn.Turtle()
ball.speed(0)
# 20 px by 20 px default
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

pen = tn.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))

pause_pen = tn.Turtle()
pause_pen.speed(0)
pause_pen.color("white")
pause_pen.penup()
pause_pen.hideturtle()
pause_pen.goto(0,0)

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y = y + 20
    else:
        y = y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y = y - 20
    else:
        y = y
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y = y + 20
    else:
        y = y
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y = y - 20
    else:
        y = y
    paddle_b.sety(y)

#this function makes the ball move faster. I'll call it everytime something gets hit.
def improve_difficulty():
    global game_speed
    if game_speed > 0.002:
        game_speed = game_speed - 0.002

def pause_handler():
    global pause
    if pause == False:
        pause = True
        pause_screen()
    else:
        pause_pen.clear()
        pause = False

def pause_screen():
    pause_pen.write("PAUSED", align="center", font=("Courier",24,"normal"))

#Listeners
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

wn.onkeypress(pause_handler, "p")

#Main Loop
pause = False
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check for borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy*(-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        improve_difficulty()


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy*(-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        improve_difficulty()


    #check for point
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,  score_b), align="center", font=("Courier",24,"normal"))
        winsound.Beep(800,300)
        #when someone makes a point speed gets reseted.
        game_speed = 0.02

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,  score_b), align="center", font=("Courier",24,"normal"))
        winsound.Beep(800,300)
        #when someone makes a point speed gets reseted.
        game_speed = 0.02

    #paddle and ball collisions
    if (ball.xcor() > 345 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40)):
        ball.setx(345)
        ball.dx = ball.dx * (-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        improve_difficulty()


    if (ball.xcor() < -345 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40)):
        ball.setx(-345)
        ball.dx = ball.dx * (-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        improve_difficulty()


    time.sleep(game_speed)
    #while pause == True:
        #time.sleep(1)
