#!/usr/bin/python3

var = 'x'

# FUNCS PARA ORDENAR
def sortPoly(polyList):
	# SORTING
	# Traverse through all array elements
	for i in range(len(polyList)):
		# Find the max element in remaining unsorted array
		max_idx = i
		for j in range(i+1, len(polyList)):
			if hasVar(polyList[j], var):
				# Si este elemento tiene una potencia > al anterior entonces swapear
				if getVarPow(polyList[j], var) > getVarPow(polyList[max_idx], var):
					max_idx = j
		# Swap the found max element with the first element
		polyList[i], polyList[max_idx] = polyList[max_idx], polyList[i]
	#return polyList
	print("Sorted poly:")
	print(polyList)
	
	# TODO: SIMPLIFY POLY --- HECHO
	newList = []
	currPow = 0
	for i in range(len(polyList)):
		element = polyList[i]
		if hasVar(element, var):
			if hasVarPow(element, var):
				# TODO: has var pow ej: +3x^2
				currPow = getVarPow(element, var)
				for j in range(i+1, len(polyList)):
					newElement = polyList[j]
					if getVarPow(newElement, var) == currPow:
						newList.append(float(element[:-3]) + float(newElement[:-3]))
			else:
				if currPow > 2:
					for i in range(currPow-2):
						newList.append(float(0))
				# TODO: has only x ej: +3x
				for j in range(i+1, len(polyList)):
					newElement = polyList[j]
					if hasVar(newElement, var) and (getVarPow(newElement, var) == 1):
						newList.append(float(element[:-1]) + float(newElement[:-1]))
		else:
			# TODO: no var ej:+3
			for j in range(i+1, len(polyList)):
				newElement = polyList[j]
				if not hasVar(newElement, var):
					newList.append(float(element) + float(newElement))
	print(newList)
	#return polyList
	#return newList
	
	# Convertir ahora la newList en formato : 3x^2 +3x +3
	polyList = []
	level = int(len(newList)-1)
	for i in range(len(newList)):
		# if have to be with a pow
		if level > 1 and i < (len(newList) - 2):
			polyList.append(str(newList[i]) + "x^" + str(level-i))
		else:
			if i < level:
				polyList.append(str(newList[i]) + "x")
			else:
				polyList.append(str(newList[i]))
	return polyList

# FUNCS PARA CALCULAR
def func(funcList, var, val):
	floatList = []
	for element in funcList:
		if hasVar(element, var):
			# Replace the value with the var
			if hasVarPow(element, var):
				# 11x^2
				floatList.append(float(float(element[:-3]) * (val**getVarPow(element, var))))
				continue
			floatList.append(float( float(element[:-1]) * val ))
			continue
		floatList.append(float(element))
	
	# Sum floatList vector
	return sum(floatList)

def calcPoly(polyList):
	for x in range(-10, 11):
		if func(polyList, var, x) == 0:
			return x

def main():
	polystr = input("Enter polynomial: ")
	if polystr == '':
		#polystr = "3x^2 -11x -4"
		#polystr = "-11x +3x^2 -4"
		polystr = "-10x +1x^2 -1x -2 +2x^2 -2"
	
	print("Your polynomial: " + polystr)
	polyList = polystr.split(' ')
	
	polyList = sortPoly(polyList)
	print("This polynomial is level " + str(float(len(polyList)-1)))
	print(polyList)
	print(calcPoly(polyList))

if __name__ == '__main__':
	main()
