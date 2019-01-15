def printAppInfo():
	print('Snake gestartet!')

def initField(numRows = 3):
	field = []

	for rowIdx in range(numRows):
		field.append('*')

	return field


# def printField(field):
	

# 	fieldString =''

# 	for row in range(len(field)):
# 		for col in range(len(field[0])):
# 			fieldString += field[row][col]

# 		fieldString += '\n'

# 	print(fieldString)


# def initField(numRows, numCols):
# 	field=[]

# 	for rowIdx in range(numRows):
# 		row = []
# 		for colIdx in range(numCols):
# 			if rowIdx == 0 or rowIdx==numRows-1 or colIdx == 0 or colIdx == numCols-1:
# 				row.append('*')
# 			else:
# 				row.append(' ')

# 		field.append(row)

# 	return field

# def get_input(text):
#     return input(text)

# def readUserInput():
# 	userInput = get_input('Enter your input:') 
# 	if userInput == 'q':
# 		#quit()
# 		print('quit')
# 		return 'quit'
# 	elif userInput == 'p':
# 		field = initField(20,40)
# 		printField(field)
# 	else:
# 		#print(userInput)
# 		print('continue')
# 		return 'continue'


# if __name__ == '__main__':
# 	while True:
# 		readUserInput()



# def testFunktion():
# 	print('ich bin eine testFunktion')

# def testQuadrat(zahl):
# 	return zahl*zahl