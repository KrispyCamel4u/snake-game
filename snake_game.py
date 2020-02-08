import turtle
import time
import random


delay = 0.08
#setting up the screen

#score 
score =0
high_score=0


window = turtle.Screen()
window.title("Snake Game by vamc")

# setting up the windows bg color and size
window.bgcolor('black')
window.setup(width=900 , height=900)


window.tracer(0) #Turns off the screen updates

#All our code logic will be between these lines

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction  = 'stop'

# Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(246,100)


segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0,410)
pen.write("Score : 0   High Score : 0", align='center',font=('Courier',24,'normal'))




#functions
def go_up():
    if head.direction!='down':
        head.direction = 'up'

def go_down():
    if head.direction!='up':
        head.direction = 'down'

def go_left():
    if head.direction!='right':
        head.direction = 'left'

def go_right():
    if head.direction!='left':
        head.direction = 'right'



def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)



#keyboard bindings 

window.listen()
window.onkeypress(go_up ,'w')
window.onkeypress(go_down ,'s')
window.onkeypress(go_left ,'a')
window.onkeypress(go_right ,'d')


# Main game loop
while True:
    window.update()


    #check for collision with wall
    if head.xcor() > 445 :
        head.goto(-445, head.ycor())
    if head.xcor() < -445:
        head.goto(445, head.ycor())
    if head.ycor() > 445:
        head.goto(head.xcor() ,-445)
    if head.ycor() < -445:
        head.goto(head.xcor() , 445)


    #check for collision with food
    if head.distance(food) <= 20:
        # Move the food to the random spot on window
        x = random.randint(-445,445)
        y = random.randint(-445,445)
        food.goto(x,y)
        delay = delay - 0.002

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        #increase the score
        score+=10

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write(f"Score : {score}   High Score : {high_score}", align='center',font=('Courier',24,'normal'))
        
    #Move the end segments first in the reverse order
    for i in range(len(segments)-1 , 0 , -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    # Move the segment 0 to where the head is
    if(len(segments) >0):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Collision with body
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = 'stop'

            #hide the segments
            for segment in segments:
                segment.goto(10000,10000)
            # clear the segments

            segments.clear()

            #Reset the score
            score=0

            #resetting the delay
            delay =0.08


            pen.clear()
            pen.write(f"Score : {score}   High Score : {high_score}", align='center',font=('Courier',24,'normal'))




    #stops the program for about 'delay' time
    time.sleep(delay) 


window.mainloop()