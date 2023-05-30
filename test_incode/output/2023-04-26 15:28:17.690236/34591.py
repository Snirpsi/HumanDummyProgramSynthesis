#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or returns a list of numbers. """    
    ports = []
    
    try:
        ports = openports()
    except OSError as e:
        print("Error: " + str(e))
        sys.exit(1)
    
    ports.sort()
    
    for port in ports:
        print(port)
        
    sys.exit(0)
    
