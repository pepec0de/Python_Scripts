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
		if getVarPow(element, var) == 2:
			if found < getVarPow(element, var):
				kind = 'quadratic'
				# Check that there is no one more greater than 2
	return kind

def hasVarPow(element, var):
	for char in element:
		if char == '^':
			return True
	return False

def getVarPow(element, var):
	isLocated = False
	for char in element:
		if isLocated:
			return float(char)
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
		eq = '3x^2 -11x -4 = 0'
	print('Your equation: ' + eq)
	eqList = eq.split(' ')
	print(checkType(eqList, var))

	# Now we split the equation in two different lists having '=' as delimiter
	e1 = []
	e2 = []
	hasFoundEqual = False
	for element in eqList:
		if element == '=':
			hasFoundEqual = True
			continue
		if not hasFoundEqual:
			e1.append(element)
		else:
			e2.append(element)

	# Kinds of equations.
	if checkType(eqList, var) == 'simple':
		# First degree method.
		# Now we sort all the elements in each corresponding list.
		# floatVar for the elements that have var
		floatVar = []
		# floatVar for the elements that do not have var
		floatVal = []
		for element in e1:
			if hasVar(element, var):
				# We use :-1 to get rid of the char
				floatVar.append(float(element[:-1]))
			else:
				floatVal.append(float(element)*-1)
		for element in e2:
			if hasVar(element, var):
				floatVar.append(float(element[:-1])*-1)
			else:
				floatVal.append(float(element))
		result = sum(floatVal) / sum(floatVar)
		print('Result: ' + str(result))
	elif checkType(eqList, var) == 'quadratic':
		# Quadratic method.
		# List creation
		floatDVar = []
		floatVar = []
		floatVal = []
		# Elements sorting
		for element in e1:
			if hasVarPow(element, var) and getVarPow(element, var) == 2:
				floatDVar.append(float(element[:-3]))
			elif hasVar(element, var) and getVarPow(element, var) == 1:
				floatVar.append(float(element[:-1]))				
			else:
				floatVal.append(float(element))
		
		for element in e2:
			if hasVarPow(element, var) and getVarPow(element, var) == 2:
				floatDVar.append(float(element[:-3])*-1)
			elif hasVar(element, var) and getVarPow(element, var) == 1:
				floatVar.append(float(element[:-1])*-1)
			else:
				floatVal.append(float(element)*-1)
		# With all elements sorted... 
		a = sum(floatDVar)
		b = sum(floatVar)
		c = sum(floatVal)
		
		# Calculate vars
		d = (b**2) - (4*a*c)
		sol = []
		sol.append( ((-b+cmath.sqrt(d)) / (2*a)) )
		sol.append( ((-b-cmath.sqrt(d)) / (2*a)) )
		print(sol)
