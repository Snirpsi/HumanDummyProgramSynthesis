#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    if number in numbers:
        print("The number is", number)
    else:
        print("The number is", numbers[number])
    
