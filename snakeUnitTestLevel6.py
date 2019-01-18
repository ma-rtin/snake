from snakeUnitTestLevel import SnakeUnitTestLevel
import unittest
from unittest.mock import patch
from io import StringIO #for mocking stdout

import snake

class SnakeUnitTestLevel6TestCase(unittest.TestCase):


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

    def test_initFieldSizeFive(self):

        field = snake.initField(numRows=5, numCols=5)

        fieldTest = [['#','#','#','#','#'],['#','','','','#'],['#','','','','#'],['#','','','','#'],['#','#','#','#','#']]
        assert fieldTest == field

    def test_initFieldSizeThree(self):

        field = snake.initField(numRows=3, numCols=3)

        fieldTest = [['#','#','#'],['#','','#'],['#','#','#']]
        assert fieldTest == field


class SnakeUnitTestLevel6(SnakeUnitTestLevel):


    def initLevel(self):
        self.levelName = 'Level 6: Spielfeld Rand erzeugen'
        task = 'Erweitere die Funktion initField().\n'
        task += 'Randelemente (1. und letzte Reihe und 1. und letzte Spalte) sollen mit \'#\' gefüllt werden .\n'
        task += 'Alle anderen Elemente sollen leer bleiben, also den Inhalt \'\' erhalten.\n'
        self.levelTask = task

    def suite(self):
        self.levelTestSuite.addTests(unittest.makeSuite(SnakeUnitTestLevel6TestCase))

        return self.levelTestSuite



