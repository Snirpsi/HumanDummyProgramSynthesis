#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    
    numbers = [int(i) for i in input().split()]
    
    for number in numbers:
        print(number)
        
