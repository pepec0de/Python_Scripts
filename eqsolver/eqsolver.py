#!/usr/bin/python3

import cmath

var = 'x'

def checkType(eqList, var):
	kind = 'simple'
	powElements = []
	for element in eqList:
		if hasVarPow(element, var):
			powElements.append(element)

	if powElements == []:
		return kind

	found = 1
	for element in powElements:
		if checkVarPow(element, var) == 2:
			if found < checkVarPow(element, var):
				kind = 'quadratic'
				# Check that there is no one more greater than 2
	return kind

def hasVarPow(element, var):
	for char in element:
		if char == '^':
			return True
	return False

def checkVarPow(element, var):
	isLocated = False
	for char in element:
		if isLocated:
			return int(char)
		if char == '^':
			isLocated = True
	return 1

# Func to check if an element has var
def hasVar(element, var):
	for char in element:
		if char.lower() == var:
			return True
	return False

if __name__ == '__main__':
	eq = input('Enter equation to solve: ')
	if eq == '':
		eq = '10x -3 = 7'
	print('Your equation: ' + eq)
	eqList = eq.split(' ')
	print(checkType(eqList, var))

	# Now we split the equation in two different lists having '=' 
	# in the middle.
	e1 = []
	e2 = []
	bE1 = True
	for element in eqList:
		if element == '=':
			bE1 = False
			continue
		if bE1 == True:
			e1.append(element)
		else:
			e2.append(element)

	# Kinds of equations.
	if checkType(eqList, var) == 'simple':
		# First degree method.
		# Now we sort all the elements in each corresponding list.
		# intVar for the elements that have var
		intVar = []
		# intVar for the elements that do not have var
		intVal = []
		for element in e1:
			if hasVar(element, var):
				# We use :-1 to get rid of the char
				intVar.append(int(element[:-1]))
			else:
				intVal.append(int(element)*-1)
		for element in e2:
			if hasVar(element, var):
				intVar.append(int(element[:-1])*-1)
			else:
				intVal.append(int(element))
		# Now we proccess the equation
		finalVar = 0
		finalVal = 0
		result = 0
		for element in intVar:
			finalVar += element

		for element in intVal:
			finalVal += element
		print('Result: ' + str(finalVal / finalVar))
	elif checkType(eqList, var) == 'quadratic':
		# Quadratic method.
		a = 0
		b = 0
		c = 0
		if bool(e1[0] == '0') != bool(e2[0] == '0'):
			# We use XOR logical operator to check that the equation is sorted
			if e1[0] == '0':
				# Then e2 has the main elements.
				for element in e2:
					if hasVarPow(element, 'x'):
						if checkVarPow(element, 'x') == 2:
							a = int(element[:-3])
					else:
						if hasVar(element, 'x'):
							b = int(element[:-1])
						else:
							c = int(element)
			else:
				# Then e1 has the main elements.
				for element in e1:
					if hasVarPow(element, 'x'):
						if checkVarPow(element, 'x') == 2:
							a = int(element[:-3])
					else:
						if hasVar(element, 'x'):
							b = int(element[:-1])
						else:
							c = int(element)              
		else:
			# Sort equation and define vars
			pass
		# Calculate vars
		d = (b**2) - (4*a*c)
		sol = []
		sol.append( ((-b+cmath.sqrt(d)) / (2*a)) )
		sol.append( ((-b-cmath.sqrt(d)) / (2*a)) )
		print(sol)
