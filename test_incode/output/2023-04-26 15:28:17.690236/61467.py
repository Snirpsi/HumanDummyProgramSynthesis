#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers or prints a port. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python ports.py <ports>")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        print("Port " + str(port))
        
