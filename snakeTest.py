#from subprocess import Popen
import subprocess

pathToSnakeFile = '/Users/martin/ownCloud/PythonLernen/'

p = subprocess.Popen(['python', 'snake.py'],cwd=pathToSnakeFile,stdout=subprocess.PIPE,
																stderr=subprocess.PIPE,
																stdin=subprocess.PIPE)
stdout, stderr = p.communicate(b'testEingabe\nquit\nq')


print('stdout:')
print(stdout)



print('Funktionstests:')

import '/Users/martin/ownCloud/PythonLernen/snake.py'

testFunktion()