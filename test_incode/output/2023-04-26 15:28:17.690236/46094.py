#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        numbers = f.read().splitlines()
        
    numbers = [int(n) for n in numbers]
    
    numbers = numbers[: