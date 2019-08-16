from game import Maze, Character, Path, blockSize
import time

grid = [
"++s+++++++++++++++++",
"++ +++++++++++++++++",
"++ +++++++++++++++++",
"++          ++++++++",
"+++++++++++ ++++++++",
"+++++++++++ ++++++++",
"+++++++++++ ++++++++",
"+++++++++++ ++++++++",
"+++++++++++ ++++++++",
"+++++++++++ ++++++++",
"+++++++++++ ++++++++",
"+++++++     ++++++++",
"+++++++ ++++++++++++",
"+++++++     ++++++++",
"+++++++++++ ++++++++",
"+++++++     ++++++++",
"+++++++ ++++++++++++",
"+       ++++++++++++",
"+ ++++++++++++++++++",
"+e++++++++++++++++++",
]

# with open("input.txt", "r") as file:
#     grid = [[str(x) for x in line] for line in file]


"""
DONOT DELETE OR EDIT THE FOLLOWING LINES
"""
maze = Maze()
maze.setUpMaze(grid)
startingPos = maze.getStartingPosition()

character = Character(startingPos)

wall = maze.getWall()

finish = maze.getFinish()

coins = maze.getCoins()

path = Path()


def checkLeft(x,y,angle):
    if angle != 180:
        return
    if(x,y) in finish:
        maze.endProgram()

    if (x , y - blockSize) not in wall:
        path.drawBlock(x,y-blockSize)
        character.rotateLeft()
        character.moveForward()
    elif (x-blockSize, y) not in wall:
        path.drawBlock(x - blockSize, y)
        character.moveForward()
    elif (x, y+blockSize) not in wall:
        path.drawBlock(x, y + blockSize)
        character.rotateRight()
        character.moveForward()
    else:
        character.rotateRight()
        character.rotateRight()

def checkRight(x,y,angle):
    if angle != 0:
        return

    if (x, y) in finish:
        maze.endProgram()

    if (x , y + blockSize) not in wall:
        path.drawBlock(x,y+blockSize)
        character.rotateLeft()
        character.moveForward()
    elif (x+blockSize, y) not in wall:
        path.drawBlock(x + blockSize, y)
        character.moveForward()
    elif (x, y-blockSize) not in wall:
        path.drawBlock(x, y - blockSize)
        character.rotateRight()
        character.moveForward()
    else:
        character.rotateRight()
        character.rotateRight()


def checkUp(x,y,angle):
    if angle != 90:
        return

    if (x, y) in finish:
        maze.endProgram()

    if (x -blockSize, y ) not in wall:
        path.drawBlock(x-blockSize,y)
        character.rotateLeft()
        character.moveForward()
    elif (x, y+blockSize) not in wall:
        path.drawBlock(x , y+blockSize)
        character.moveForward()
    elif (x+blockSize, y) not in wall:
        path.drawBlock(x+blockSize, y)
        character.rotateRight()
        character.moveForward()
    else:
        character.rotateRight()
        character.rotateRight()


def checkDown(x,y,angle):
    if  angle !=  270:
        return

    if (x, y) in finish:
        maze.endProgram()

    if (x +blockSize, y ) not in wall:
        path.drawBlock(x+blockSize,y)
        character.rotateLeft()
        character.moveForward()
    elif (x, y-blockSize) not in wall:
        path.drawBlock(x , y-blockSize)
        character.moveForward()
    elif (x-blockSize, y) not in wall:
        path.drawBlock(x-blockSize, y )
        character.rotateRight()
        character.moveForward()
    else:
        character.rotateRight()
        character.rotateRight()




while(True):
    """
    * You have the coordinates of the walls stored in "wall" list in the form of tuples [(x,y), (i,j)] -- list of tuples

    * You have the coordinates of the end point stored in "finish" tuple in the form of (x,y)

    * You have the coordinates of the coins stored in "coins" list in the form of tuples [(x,y), (i,j)] -- list of tuples

    * At each itteration you get the following:
        - X coordinate of the character stored in "currentX" variable
        - Y coordinate of the character stored in "currentY" variable
        - Current angle of the character stored in "angle" variable

    * To move the character forward write character.moveForward()

    * To rotate the character to the right write character.rotateRight()

    * To rotate the character to the left write character.rotateLeft()

    * To update the coordinates after moving write the following lines:
        -   currentX = character.getCurrentX()
        -   currentY = character.getCurrentY()

    * To update the angle after rotating write the following line:
        -   angle = character.getAngle()

    * To draw the path you can use either of the following functions:
        - path.drawBlock(x,y) to draw a box on x,y coordinates
        - path.drawArray(array) to draw a series of boxes by passing a list that contains a
        tuple of coordinates i.e.
                array = [(10,20), (5, 30)]
                path.drawArray(array) #this will draw two blue boxes one at(10,20) and the other at (5,30)


    * The angles are illustrated below


                            angle  = 90
                                |
                                |
                                |
                   _____________|_____________
         angle = 180            |           angle = 0
                                |
                                |
                                |
                            angle = 270

    * To end the game break from the while loop
    """

    currentX = character.getCurrentX()
    currentY = character.getCurrentY()
    angle = character.getAngle()
    print("X: " + str(currentX) + " Y: " + str(currentY) + " Angle: " + str(angle))
    ################## WRITE YOUR CODE BELOW ##########################

    checkLeft(currentX,currentY,angle)
    currentX = character.getCurrentX()
    currentY = character.getCurrentY()
    angle = character.getAngle()
    checkRight(currentX, currentY, angle)
    currentX = character.getCurrentX()
    currentY = character.getCurrentY()
    angle = character.getAngle()
    checkUp(currentX, currentY, angle)
    currentX = character.getCurrentX()
    currentY = character.getCurrentY()
    angle = character.getAngle()
    checkDown(currentX, currentY, angle)


    ###################################################################


"""
DONOT DELETE THE FOLLOWING LINE
"""
maze.endProgram()
