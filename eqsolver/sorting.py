#!/usr/bin/python3
import sys

def sortArrayMaxToMin(arr):
    print("Array without sorting")
    print(arr)
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the max element in remaining unsorted array
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # Swap the found max element with the first element
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def main1():
    # Python program for implementation of Selection
    # Sort  
    A = [64, 25, 12, 22, 11] 
    print("Array without sorting")
    print(A)
    # Traverse through all array elements 
    for i in range(len(A)): 
      
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] < A[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i] 
  
    # Driver code to test above 
    print ("Sorted array") 
    #for i in range(len(A)): print("%d" %A[i])
    print(A)

def main():
    print(sortArrayMaxToMin([22, 11, 64, 25, 12, 43]))
if __name__ == '__main__':
    main()
