#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port. """    
    
    port = int(sys.argv[1])
    
    multiplier = 1
    
    for i in range(port):
        multiplier = multiplier * i
    
    print(multiplier)
    
