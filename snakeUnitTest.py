import unittest

from unittest.mock import patch

from io import StringIO #for mocking stdout

import snake


class Level1Test(unittest.TestCase):

    def test_2(self):
    	self.assertEqual(snake.testQuadrat(3),9)


    @patch('snake.get_input', return_value='q')
    def test_inputQuit(self, input):
        self.assertEqual(snake.readUserInput(), 'quit')

    @patch('snake.get_input', return_value='c')
    def test_inputContinue(self, input):
        self.assertEqual(snake.readUserInput(), 'continue')


    @patch('sys.stdout', new_callable=StringIO)
    def test_stdOut(self, mock_stdout):
	    snake.testFunktion()
	    assert mock_stdout.getvalue() == 'ich bin eine testFunktion\n'

    @patch('sys.stdout', new_callable=StringIO)
    def test_printFieldSmall(self, mock_stdout):
        field = snake.initField(1,4)
        snake.printField(field)
        returnStr = mock_stdout.getvalue()
        assert returnStr.strip() == '****'

    @patch('sys.stdout', new_callable=StringIO)
    def test_printFieldLarge(self, mock_stdout):
        field = snake.initField(3,3)
        snake.printField(field)
        assert mock_stdout.getvalue() == '***\n* *\n***\n\n'


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Level1Test('test_printFieldSmall'))
    suite.addTest(Level1Test('test_printFieldLarge'))
    return suite


if __name__ == '__main__':
#    unittest.main()
    runner = unittest.TextTestRunner(verbosity=3)

    level1Suite = suite()

    test_result = runner.run(level1Suite)


    print(test_result)

    for t in test_result.failures:
    	print(t[0].id())
