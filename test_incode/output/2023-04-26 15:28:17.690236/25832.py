#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python port-calculator.py <port>")
        exit(1)
    
    port = sys.argv[1]
    
    print("Calculating port 