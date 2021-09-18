######################################################################
# Author: Beau Schneider
# Username: schneiderb 
#
# Assignment: p01-BeauSchneider
#
# Purpose:  To let the user play a version of a Snake game and use keyboard controls 
#             to move player and collect candies.
            
######################################################################
# Acknowledgements:
#
# Original Author: Beau Schneider
####################################################################################
import turtle
import random
global snake





# Screen Setup
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("This > The Snake Game")

class Cube(turtle.Turtle):
    """
    This is the class for the 'candy' that the player has to eat to gain score
    this Cube moves each time the player comes into contact with it
    and gives the player 10 points.
    This also triggers the red cubes to move to a new position.
    """

    def __init__(self):
        """
        This sets the attributes for the candy in the game
        """
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.pensize(20)
        self.speed(0)


    def cube_position(self):
        """
        This is what is used to get the candy once its 'eaten' to go to a new coordinate
        on the screen.
        """
        self.penup()
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)


class Cubetwo(turtle.Turtle):
    """
    This is one of the stationary red cubes that spawn
    in the play able area around the player
    to force them to navigate around them
    and die if they come into contact with them
    """

    def __init__(self):
        """
        This is what is used to set the attributes for the stationary enemy
        on the screen.
        """
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.pensize(20)
        self.speed(0)

    def cube2_position(self):
        """
        This is used to set the red cube enemies to move to a random point on the screen
        whenever the game first starts and everytime the 'candy' is eaten.
        """
        self.penup()
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)


class Cubethree(turtle.Turtle):
    """
    This is one of the stationary red cubes that spawn
    in the play able area around the player
    to force them to navigate around them
    and die if they come into contact with them
    """

    def __init__(self):
        """
        This is what is used to set the attributes for the stationary enemy
        on the screen.
        """
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.pensize(20)
        self.speed(0)

    def cubethree_position(self):
        """
        This is used to set the red cube enemies to move to a random point on the screen
        whenever the game first starts and everytime the 'candy' is eaten.
        """
        self.penup()
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)

class Cubefour(turtle.Turtle):
    """
    This is one of the stationary red cubes that spawn
    in the play able area around the player
    to force them to navigate around them
    and die if they come into contact with them
    """

    def __init__(self):
        """
        This is what is used to set the attributes for the stationary enemy
        on the screen.
        """
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.pensize(20)
        self.speed(0)


    def cubefour_position(self):
        """
        This is used to set the red cube enemies to move to a random point on the screen
        whenever the game first starts and everytime the 'candy' is eaten.
        """
        self.penup()
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)


class Cube_Tracker(turtle.Turtle):
    """
    This is the class for the enemy that follows the player on the screen
    if the player gets touched by this enemy the player dies.
    """

    def __init__(self):
        """
        This tells the enemy to go to a random point on the screen
        and sets all attributes for the enemy
        """
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("red")
        self.pensize(20)
        self.speed(0)
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)





class Pen():
    """
    This class is used to draw the score at the top of the window
    and close the window if the player dies
    """

    def __init__(self):
        """
        Creates turtle and sets score value to 0
        """
        self.score = 0
        self.pen = turtle.Turtle()

    def draw_score(self):
        """
        This draws the score at the top of the window
        and updates whenever the player gets a 'candy'.
        """
        self.pen.reset()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write(" Score: " + str(self.score), align="center", font=("Courier", 30, "normal"))

    def player_dead(self):
        """
        This closes the window whenever the player dies
        """
        wn.bye()
        wn.mainloop()




class Border(turtle.Turtle):
    """
    This class is for drawing the border to define playable area
    and setting the attributes for the border when drawn.
    """

    def __init__(self):
        """
        This sets the attributes for the border
        """
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("black")
        self.pensize(5)


    def draw_border(self):
        """
        This draws the border to show to playable area for the player.
        """
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)



class Snake(turtle.Turtle):
    """
    This is the 'player' class and defines all movement, interaction, and score
    for the player.
    """

    def __init__(self):
        """
        This sets the attributes for the player
        """
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("turtle")
        self.color('yellow')
        self.speed(8)
        self.pensize(20)

    def move_forward(self):
        """
        This defines the speed of the player and checks constantly
        to see if the player is dead or if the player has come into
        contact with the candy and gives score if needed.
        This class also handles all keybindings that the user will use
        to control he player on the screen.
        """

        self.forward(5)

        # Checking borders and dying if comes in contact

        if self.xcor() > 290 or self.xcor() < -290:
            pen.player_dead()

        if self.ycor() > 290 or self.ycor() < -290:
            pen.player_dead()

        # Checks to see if player has come into contact with the red cubes or the enemy

        if player.distance(cube) < 20:
            cube.cube_position()
            cube2.cube2_position()
            cube3.cubethree_position()
            cube4.cubefour_position()
            pen.score += 10

            pen.draw_score()

        if player.distance(cube2) < 20:
            pen.player_dead()

        if player.distance(enemy) < 20:
            pen.player_dead()

        if player.distance(cube3) < 20:
            pen.player_dead()

        if player.distance(cube4) <20:
            pen.player_dead()

        # This is the methods used when the user presses specific bound keys

    def turnleft(self):
        """
        If user presses key 'Left' the player turns 90 degrees left
        """
        self.left(90)
        self.speed(1)

    def turnright(self):
        """
        If the user presses the 'Right' key the player turns
        90 degrees to the right.
        """
        self.right(90)
        self.speed(1)

    def turnaround(self):
        """
        If the user presses the 'down' key the player
        will turn 180 degrees (completely around)
        """
        self.right(180)
        self.speed(1)
    def playerquit(self):
        """
        If the user presses the 'q' key the program will quit
        and the window will close.
        """
        wn.bye()
        quit()
    def follow_player(self):
        """
        This is the method that calls the Cube_Tracker method
        to follow the coordinates of the player around on the screen.
        """
        enemy.penup()
        enemy.setheading(enemy.towards(self))
        enemy.forward(4)


# redefines player class instance to allow for
# and easier time using commands.
player = Snake()
border = Border()
pen = Pen()
cube = Cube()
cube2 = Cubetwo()
enemy = Cube_Tracker()
cube3 = Cubethree()
cube4 = Cubefour()


# draw border and position cube on screen
# This all happens before the game starts once the player button is clicked.
border.draw_border()
cube.cube_position()
pen.draw_score()
cube2.cube2_position()
cube3.cubethree_position()
cube4.cubefour_position()


# Defines all key bindings for user control of Snake class.
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.playerquit, "q")
turtle.onkey(player.turnaround, "Down")


# infinite loop, makes player always move forward and enemy always follow the player
# Calls the turtle to listen for user keyboard inputs and call the corresponding
# Snake method.
while True:
    turtle.listen()
    player.move_forward()
    player.follow_player()














