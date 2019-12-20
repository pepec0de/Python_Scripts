#!/usr/bin/python3

import cmath

var = 'x'

# Func to process the type of an input
def checkType(eqList, var):
	kind = 'simple'
	powElements = []
	for element in eqList:
		if hasVarPow(element, var):
			powElements.append(element)
	# If there aren't any var with a pow (2x = 4)
	if powElements == []:
		return kind

	found = 1
	for element in powElements:
		if getVarPow(element, var) == 2:
			if found < getVarPow(element, var):
				kind = 'quadratic'
				# Check that there is no one more greater than 2
	return kind

# Func to check if there is a ^pow^ in an element with var
def hasVarPow(element, var):
	if hasVar(element, var):
		for char in element:
			if char == '^':
				return True
	return False

# Func to get the ^pow^ of an element with var (3x^2)
def getVarPow(element, var):
	if hasVar(element, var):
		isLocated = False
		for char in element:
			if isLocated:
				return float(char)
			if char == '^':
				isLocated = True
		return 1
	return 0

# Func to check if an element has var
def hasVar(element, var):
	for char in element:
		if char.lower() == var:
			return True
	return False

def main():
	eq = input('Enter equation to solve: ')
	if eq == '':
		eq = '3x^2 -11x -4 = 0'
	print('Your equation: ' + eq)
	eqList = eq.split(' ')
	print(checkType(eqList, var))

	# Now we split the equation in two different lists having '=' 
	# in the middle.
	e1 = []
	e2 = []
	hasFoundEqual = False
	for element in eqList:
		if element == '=':
			hasFoundEqual = True
			# We use continue to not appending '=' in the element's list
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

if __name__ == '__main__':
	main()
	quit()
