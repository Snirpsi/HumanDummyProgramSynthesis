#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers. """    
    numbers = []
    
    for _ in range(int(input())):
        numbers.append(int(input()))
    
    print(numbers)
    
