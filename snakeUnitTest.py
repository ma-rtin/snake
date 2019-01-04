import unittest


from snakeUnitTestLevel1 import SnakeUnitTestLevel1


if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=3)

    

    level1 = SnakeUnitTestLevel1()
    level1Suite = level1.suite()
    test_result = runner.run(level1Suite)

    print(test_result)

    #for t in test_result.failures:
    	#print(t[0].id())

    if len(test_result.failures)>0 or len(test_result.errors)>0:
        level1.successMessage()
        # print('#########################################################')
        # print('#########################################################')
        # print('#########################################################')
        # print('')
        # print('')
        # print('')
        # print('level 1 geschafft! (Python Programm öffnen)')
        # print('')
        # print('nächstes Level: Schreibe eine Funtion printInfo die folgenden Text ausgibt: \"Snake.py erfolgreich gestartet\"')
        # print('')
        # print('')
