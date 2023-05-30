#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    if number > 100 or number < 0:
        print("Invalid number")
    else:
        print(number)
    
