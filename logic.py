from game import Maze, Character
import time

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


maze = Maze()
maze.setUpMaze(grid)
startingPos = maze.getStartingPosition()
ch = Character(startingPos)
wall = maze.getWall()
finish = maze.getFinish()
counter = 0


while(True):
    """
    write your code here
    """
    maze.endProgram
