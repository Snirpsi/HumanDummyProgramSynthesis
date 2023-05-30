#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
        
    
