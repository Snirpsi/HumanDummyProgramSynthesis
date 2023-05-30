#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        exit(1)
    
    numbers = sys.argv[1].split(",")
    
    numbers = [float(x) for x in numbers]
    
    numbers_