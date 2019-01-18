from snakeUnitTestLevel import SnakeUnitTestLevel
import unittest
from unittest.mock import patch
from io import StringIO #for mocking stdout

import snake

class SnakeUnitTestLevel5TestCase(unittest.TestCase):


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

        assert len(field[0]) == 5

    def test_initFieldSizeTwenty(self):

        field = snake.initField(numRows=20, numCols=20)

        assert len(field[0]) == 20

class SnakeUnitTestLevel5(SnakeUnitTestLevel):


    def initLevel(self):
        self.levelName = 'Level 5: Spielfeld erzeugen (2-Dimensional)'
        task = 'Erweitere die Funktion initField().\n'
        task += 'Sie soll ein Übergabeparameter numCols erhalten, der die Breite des Spielfelds angibt.\n'
        task += 'Der Übergabeparameter soll optional sein und den Wert 1 annehmen, falls er nicht übergeben wird.\n'
        task += 'Die Funktionsdefinition soll also\n\n'
        task += 'def initField(numRows=3, numCols=1):\n'
        task += '    ...\n'
        task += '    return field\n\n'
        task += 'lauten. (Bei ... muss dein eigener Code eingefügt werden)\n'
        task += 'Der Inhalt der Liste spielt keine Rolle'
        self.levelTask = task

    def suite(self):
        self.levelTestSuite.addTests(unittest.makeSuite(SnakeUnitTestLevel5TestCase))

        return self.levelTestSuite



