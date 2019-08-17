#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'pepesource'

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
    if checkType(eqList, var) == 'simple':
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
        # Quadratic method
        # We use XOR logical operator
        if bool(e1[0] == '0') != bool(e2[0] == '0'):
            # Equation sorting


