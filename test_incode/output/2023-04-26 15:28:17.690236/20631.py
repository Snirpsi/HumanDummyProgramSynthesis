#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    number = sys.argv[1]
    
    if number.isdigit():
        number = int(number)
        
        print(number)
    else:
        print("Invalid number.")
    
