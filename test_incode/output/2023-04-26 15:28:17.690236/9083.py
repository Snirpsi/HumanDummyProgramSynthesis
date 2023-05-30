#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and converts fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s fruits.txt" % sys.argv[0])
        sys.exit()
    
    with open(sys.argv[1], 'r') as fruits:
        fruits = [line.strip() for line in fruits]
        
        fruits_converted = []
        for fruit in fruits:
            fruits_converted.append(