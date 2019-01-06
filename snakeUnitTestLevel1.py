from snakeUnitTestLevel import SnakeUnitTestLevel
import unittest
from unittest.mock import patch
from io import StringIO #for mocking stdout

import snake

class SnakeUnitTestLevel1TestCase(unittest.TestCase):
    def test_2(self):
        self.assertEqual(snake.testQuadrat(3),9)


    # @patch('snake.get_input', return_value='q')
    # def test_inputQuit(self, input):
    #     self.assertEqual(snake.readUserInput(), 'quit')

    # @patch('snake.get_input', return_value='c')
    # def test_inputContinue(self, input):
    #     self.assertEqual(snake.readUserInput(), 'continue')


    # @patch('sys.stdout', new_callable=StringIO)
    # def test_stdOut(self, mock_stdout):
	   #  snake.testFunktion()
	   #  assert mock_stdout.getvalue() == 'ich bin eine testFunktion\n'

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_printFieldSmall(self, mock_stdout):
    #     field = snake.initField(1,4)
    #     snake.printField(field)
    #     returnStr = mock_stdout.getvalue()
    #     assert returnStr.strip() == '****'

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_printFieldLarge(self, mock_stdout):
    #     field = snake.initField(3,3)
    #     snake.printField(field)
    #     assert mock_stdout.getvalue() == '***\n* *\n***\n\n'

class SnakeUnitTestLevel1(SnakeUnitTestLevel):


    def initLevel(self):
    	self.levelName = 'Level 1: Python Programm öffnen'

    # simple runLevel and evaluateLevel method for first level
    # no tests have to be successful
    # level 1 is just about running the python script
    def runLevel(self):
    	return None

    def evaluateLevel(self):
        self.successMessage()
        self.levelCompleted = True



