#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    if number > 0 and number < 10:
        print(number)
    else:
        print("Invalid number")
    
