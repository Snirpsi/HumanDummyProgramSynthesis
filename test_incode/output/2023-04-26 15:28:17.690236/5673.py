#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or stores numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    for x in range(port):
        print(str(x