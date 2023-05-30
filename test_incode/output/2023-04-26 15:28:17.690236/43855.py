#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and calculates fruits. """    
    port = int(sys.argv[1])
    fruits = fruitsCalculator(port)
    print("The fruits are: ", fruits)
