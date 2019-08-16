from game import Maze, Character, Path
import time

# grid = [
# "++s+++++++++++++++++",
# "++ ++++ +++++++ ++++",
# "++ ++++ +++++++ ++++",
# "++   x      +++ ++++",
# "+++ +++++++ +++ x  +",
# "+++ +++++++ ++++++++",
# "+++x+++++++ ++++++++",
# "+++ +++++++      +++",
# "+++  x+++++ ++++ +++",
# "+++ +++++++ ++++x+++",
# "+   +++++++ ++++ +++",
# "+++ +++     ++++++++",
# "+++ +++ ++++++++++++",
# "+++ +++     ++++++++",
# "+++ +++++++ ++++++++",
# "+++ +++       x  +++",
# "+++ +++ ++++++++++++",
# "+   x   ++++++++++++",
# "+ ++++++++++++++++++",
# "+e++++++++++++++++++",
# ]

with open("input.txt", "r") as file:
    grid = [[str(x) for x in line] for line in file]

maze = Maze()
maze.setUpMaze(grid)
startingPos = maze.getStartingPosition()

character = Character(startingPos)

wall = maze.getWall()

finish = maze.getFinish()

path = Path()

counter = 0
stepSize = 24
list = []

while(True):
    """
    * You have the coordinates of the wall stored in "wall" list in the form of a tuple (x,y)

    * You have the coordinates of the finish point stored in "finish" list in the form of [x,y]

    * At each itteration you get the following:
        - X coordinate of the character stored in currentX variable
        - Y coordinate of the character stored in currentY variable

    * To move a character to a certain point write character.moveTo(x,y)

    * To draw the path you can use either of the following functions:
        - path.drawBlock(x,y) to draw a box on x,y coordinates
        - path.drawArray(array) to draw a series of boxes by passing a list that contains a
        tuple of coordinates i.e.
                array = [(10,20), (5, 30)]
                path.drawArray(array) #this will draw two blue boxes one at(10,20) and the other at (5,30)

    """
    currentX = character.getCurrentX()
    currentY = character.getCurrentY()

    ################## WRITE YOUR CODE BELOW ##########################



    ###################################################################

    """
    DONOT DELETE THE FOLLOWING LINE
    """
    maze.endProgram()
