#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or prints numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 list.py [numbers]")
    else:
        numbers = sys.argv[1:]
        
        for number in numbers:
            print(number)
    
