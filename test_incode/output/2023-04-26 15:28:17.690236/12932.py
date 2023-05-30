#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    
    numbers = [int(i) for i in input("Enter a number: ").split()]
    
    for number in numbers:
        print(number, end=' ')
    
    print("\nDone!")
    
