#!/usr/bin/python3

from utils import *

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
	sol = 0
	for element in floatList:
		sol = sol + element
	return sol

def main():
	funcstr = input("Enter func: ")
	if funcstr == '':
		funcstr = "-11x +3x^4 -4"

	print("Your func: " + funcstr)

	value = float(input("Value: "))
	print(funcstr.replace("x", "*"+str(value)))
	
	print(func(funcstr.split(' '), 'x', value))

if __name__ == '__main__':
	main()
