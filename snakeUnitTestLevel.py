import unittest
#from unittest.mock import patch
#from io import StringIO #for mocking stdout



class SnakeUnitTestLevel():

    def __init__(self):
        self.levelTestSuite = unittest.TestSuite()

        self.initLevel()

        self.test_result = None

        self.levelCompleted = False


    def initLevel(self):
    	self.levelName = ''
    	self.levelTask = ''

    def runLevel(self):
        print('\nStarte ('+self.levelName+')...\n\n')

        
        print('--------------------------------------------------')
        print('Unit tests of ('+self.levelName+'):')
        print('--------------------------------------------------')
        print('')

        runner = unittest.TextTestRunner(verbosity=0)
        levelSuite = self.suite()
        self.test_result = runner.run(levelSuite)

        print('--------------------------------------------------')
        print('--------------------------------------------------')
        print('--------------------------------------------------')
        print('')
        #print(self.test_result)

    def evaluateLevel(self):
        if len(self.test_result.failures)==0 and len(self.test_result.errors)==0:
            self.successMessage()
            self.levelCompleted = True
        else:
        	print('('+self.levelName + ') nicht erfolgreich\n\n')
        	print('Aufgabe für dieses Level:')
        	print(self.levelTask)
        #print('Level evaluated')

    def successMessage(self):
        print('#########################################################')
        print('#########################################################')
        print('Level geschafft! ('+self.levelName+')')
        print('#########################################################')
        print('#########################################################')
        print('#########################################################')

    def suite(self):
    	return None
