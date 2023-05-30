#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Store numbers in an array
    numbers_array = numbers[:]
    
    # Print the numbers in the array
    print(numbers_array)
    
    # Print the length of numbers_array
    print(len(numbers_array))
    
    # Print the maximum number in the array
    print(max(numbers_array))
    
    # Print the minimum number in the array
    print(min(numbers_array))
    
    # Print the average of the numbers in the array
    print(sum(numbers_array)/len(numbers_array))
    
    # Print the sum of squares of the numbers in the array
    print(sum(numbers_array**2)