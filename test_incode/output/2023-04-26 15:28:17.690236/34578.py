#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or multiplyes words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = sys.argv[1]
        
        if number.isdigit():
            number = int(number)
            
            print(number * "*")
        else:
            print(number.upper())
    else:
        print("Usage: python3 number