from snakeUnitTestLevel import SnakeUnitTestLevel
import unittest
from unittest.mock import patch
from io import StringIO #for mocking stdout

import snake

class SnakeUnitTestLevel3TestCase(unittest.TestCase):


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

    def test_initFieldSize(self):

        field = snake.initField()

        assert len(field) == 3

        

    def test_initFieldType(self):

        field = snake.initField()

        assert isinstance(field,list)

class SnakeUnitTestLevel3(SnakeUnitTestLevel):


    def initLevel(self):
        self.levelName = 'Level 3: Spielfeld erzeugen'
        task = 'Schreibe eine Funktion initField(), die eine Liste mit 3 Elementen zurückgibt.'
        self.levelTask = task

    def suite(self):
        self.levelTestSuite.addTests(unittest.makeSuite(SnakeUnitTestLevel3TestCase))

        return self.levelTestSuite



