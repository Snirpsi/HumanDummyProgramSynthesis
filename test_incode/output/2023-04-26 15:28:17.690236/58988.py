#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    numbers = [int(i) for i in open('numbers.txt')]
    
    # Print the numbers in reverse order
    for n in numbers[::-1]:
        print(n)
        
    # Print the numbers in ascending order
    for n in numbers:
        print(n)
        
    # Print the numbers in reverse and ascending order
    for n in numbers[::-1] + numbers:
        print(n)
        
    # Print the numbers in reverse and descending order
    for n in numbers[::-1] + numbers[::-1]:
        print(n)
        
    # Print the numbers in ascending order and descending order
    for n in numbers[::-1] + numbers[::-1] + numbers:
        print(n)
        
    # Print the numbers in ascending order and descending order and reverse order
    for n in numbers[::-1] + numbers[::-1] + numbers[::-1]:
        print(n)
        
    # Print the numbers in ascending order and descending order and reverse order and ascending order
    for n in numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1]:
        print(n)
        
    # Print the numbers in ascending order and descending order and reverse order and ascending order and descending order
    for n in numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1]:
        print(n)
        
    # Print the numbers in ascending order and descending order and reverse order and ascending order and descending order and reverse order
    for n in numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1] + numbers[::-1]:
        print(n)
        
    # Print the numbers in ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending order and reverse order and ascending order and descending 