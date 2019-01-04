import unittest
#from unittest.mock import patch
#from io import StringIO #for mocking stdout



class SnakeUnitTestLevel():

    def __init__(self):
        self.levelTestSuite = unittest.TestSuite()

        self.setLevelName()

    def setLevelName(self):
    	self.levelName = ''

    def successMessage(self):
        print('#########################################################')
        print('#########################################################')
        print('#########################################################')
        print('')
        print('')
        print('')
        print('Level 1 geschafft! ('+self.levelName+')')
