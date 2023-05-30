#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruits>" % sys.argv[0])
        sys.exit(0)
    
    fruits = sys.argv[1:]
    
    numbers = []
    for fruit in fruits:
        numbers.append(int(