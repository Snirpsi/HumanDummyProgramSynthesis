#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    numbers = [number] * int(input("Enter a number: "))
    
    print("The product of the numbers is ", numbers)
    
