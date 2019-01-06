
from snakeUnitTestLevel1 import SnakeUnitTestLevel1
from snakeUnitTestLevel2 import SnakeUnitTestLevel2

if __name__ == '__main__':

    levels = []
    levels.append(SnakeUnitTestLevel1())
    levels.append(SnakeUnitTestLevel2())

    for level in levels:
        level.runLevel()
        level.evaluateLevel()