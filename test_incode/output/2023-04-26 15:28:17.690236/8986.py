#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and calculates fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    fruits = calc_fruits(port)
    
    print("The port is {} and the fruits are: {}"
          .format(port, fruits))
    
