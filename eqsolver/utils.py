#!/usr/bin/python3

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
