#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or prints all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        ports = openports()
    else:
        ports = openports(sys.argv[1])
    
    for port in ports:
        print(port)
        
