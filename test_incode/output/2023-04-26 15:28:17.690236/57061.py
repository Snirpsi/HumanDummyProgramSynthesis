#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python portCalculator.py <port>")
        
    else:
        port = int(sys.argv[1])
        
        portCalculator(port)
        
