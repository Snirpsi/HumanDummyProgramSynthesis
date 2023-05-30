#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and stores numbers. """    
    ports = [int(x) for x in sys.argv[1:]]
    
    for port in ports:
        print(port)
        
