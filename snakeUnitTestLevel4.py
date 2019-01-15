from snakeUnitTestLevel import SnakeUnitTestLevel
import unittest
from unittest.mock import patch
from io import StringIO #for mocking stdout

import snake

class SnakeUnitTestLevel4TestCase(unittest.TestCase):


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

        field = snake.initField(numRows=5)

        assert len(field) == 5

    def test_initFieldSizeTwenty(self):

        field = snake.initField(numRows=20)

        assert len(field) == 20

class SnakeUnitTestLevel4(SnakeUnitTestLevel):


    def initLevel(self):
        self.levelName = 'Level 4: Spielfeld erzeugen'
        task = 'Erweitere die Funktion initField().\n'
        task += 'Sie soll ein Übergabeparameter numRows erhalten, der die Länge der Liste angibt.\n'
        task += 'Der Übergabeparameter soll optional sein und den Wert 3 annehmen, falls er nicht übergeben wird.\n'
        task += 'Die Funktionsdefinition soll also\n\n'
        task += 'def initField(numRows=3):\n'
        task += '    ...\n'
        task += '    return field\n\n'
        task += 'lauten. (Bei ... muss dein eigener Code eingefügt werden)\n'
        task += 'Der Inhalt der Liste spielt keine Rolle'
        self.levelTask = task

    def suite(self):
        self.levelTestSuite.addTests(unittest.makeSuite(SnakeUnitTestLevel4TestCase))

        return self.levelTestSuite



