#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    import sys
    numbers = sys.argv[1:]
    numbers = [int(x) for x in numbers]
    
    for number in numbers:
        print(number)
        
