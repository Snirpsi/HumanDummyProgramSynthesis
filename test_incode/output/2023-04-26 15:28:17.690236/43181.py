#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Print the list of numbers:
    print(numbers)
    
    # Print the sum of all numbers:
    print(sum(numbers))
    
    # Print the average of all numbers:
    print(sum(numbers)/len(numbers))
    
    # Print the difference of all numbers:
    print(sum(numbers)-sum(numbers[:len(numbers)//2]))
    
    # Print the difference of all numbers, starting from index 1:
    print(sum(numbers)-sum(numbers[:len(numbers)//2]