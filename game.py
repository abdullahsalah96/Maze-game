import turtle                    # import turtle library
import time
import sys
import collections

class Maze():
    def __init__(self):
        self.bg = turtle.Screen()
        self.bg.bgcolor("black")
        self.bg.setup(700,600)
        self.grid = turtle.Turtle()
        self.grid.shape("square")
        self.grid.color("white")
        self.grid.penup()
        self.grid.speed(0)
        self.end = turtle.Turtle()
        self.end.shape("square")
        self.end.color("green")
        self.end.penup()
        self.grid.speed(0)
        self.wall = []
        self.finish = []
        self.startX = -250
        self.startY = 250

    def setUpMaze(self, border):
        for y in range(len(border)):
            for x in range(len(border[y])):
                square = border[y][x]
                screen_x = self.startX + (x * 24)               # assign screen_x to screen starting position for x ie -588
                screen_y = self.startY - (y * 24)                # assign screen_y to screen starting position for y ie  288
                if square == "+":                     # if grid character contains an +
                    self.grid.goto(screen_x, screen_y)        # move turtle to the x and y location and
                    self.grid.stamp()                         # stamp a copy of the turtle (white square) on the screen
                    self.wall.append((screen_x, screen_y))   # add coordinate to walls list
                elif square == "e":                     # if grid character contains an e
                    self.end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                    self.end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                    self.finish.append((screen_x, screen_y))  # add coordinate to finish list
                #
                # elif character == "s":                     # if the grid character contains an s
                #     sprite.goto(screen_x, screen_y)      # move turtle to the x and y location
                #     visited.append((screen_x,screen_y))
                #     sprite.x = screen_x
                #     sprite.y = screen_y
                #
                # elif character == "x":                     # if the grid character contains an s
                #     path.goto(screen_x, screen_y)  # move turtle to the x and y location and
                #     path.stamp()  # stamp a copy of the turtle (white square) on the screen
                #
    def getWall(self):
        return self.wall

    def getStartX(self):
        return self.startX

    def getStartY(self):
        return self.startY

    def getFinish(self):
        return self.finish

grid = [
"++s+++++++++++++++++",
"++ ++++ +++++++ ++++",
"++ ++++ +++++++ ++++",
"++   x      +++ ++++",
"+++ +++++++ +++ x  +",
"+++ +++++++ ++++++++",
"+++x+++++++ ++++++++",
"+++ +++++++      +++",
"+++  x+++++ ++++ +++",
"+++ +++++++ ++++x+++",
"+   +++++++ ++++ +++",
"+++ +++     ++++++++",
"+++ +++ ++++++++++++",
"+++ +++     ++++++++",
"+++ +++++++ ++++++++",
"+++ +++       x  +++",
"+++ +++ ++++++++++++",
"+   x   ++++++++++++",
"+ ++++++++++++++++++",
"+e++++++++++++++++++",
]

m = Maze()
m.setUpMaze(grid)
