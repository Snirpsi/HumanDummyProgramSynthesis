#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and calculates a list of words. """    
    
    # Read input from stdin
    numbers = map(int, sys.stdin.readline().split())
    
    # Convert numbers to words
    words = map(str, numbers)
    
    # Print the words
    print(*words, sep='\n')
    
    # Print the sum of the numbers
    print(sum(numbers))
    
    # Print the average of the numbers
    print(sum(numbers)/len(numbers))
    
    # Print the sum of the squares of the numbers
    print(sum(map(lambda x: x**2, numbers)))
    
    # Print the average of the squares of the numbers
    print(sum(map(lambda x: x**2, numbers))/len(numbers))
    
    # Print the sum of the cubes of the numbers
    print(sum(map(lambda x: x**3, numbers)))
    
    # Print the average of the cubes of the numbers
    print(sum(map(lambda x: x**3, numbers))/len(numbers))
    
    # Print the sum of the squares of the cubes of the numbers
    print(sum(map(lambda x: x**