from snakeUnitTestLevel import SnakeUnitTestLevel
import unittest
from unittest.mock import patch
from io import StringIO #for mocking stdout

import snake

class SnakeUnitTestLevel2TestCase(unittest.TestCase):


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

    @patch('sys.stdout', new_callable=StringIO)
    def test_printAppInfo(self, mock_stdout):

        snake.printAppInfo()

        printAppInfoOutput = mock_stdout.getvalue()
        assert printAppInfoOutput == 'Snake gestartet!\n'

class SnakeUnitTestLevel2(SnakeUnitTestLevel):


    def initLevel(self):
        self.levelName = 'Level 2: Programm Info ausgeben'
        task = 'Schreibe eine Funktion printAppInfo(), die in der Konsole \"Snake gestartet!\" ausgibt.'
        self.levelTask = task

    def suite(self):
        self.levelTestSuite.addTests(unittest.makeSuite(SnakeUnitTestLevel2TestCase))

        return self.levelTestSuite



