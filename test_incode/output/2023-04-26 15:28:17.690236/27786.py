#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
    else:
        numbers = input("Enter numbers: ").split()
    
    for number in numbers:
        print(number)
    
