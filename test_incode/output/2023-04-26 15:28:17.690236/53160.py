#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and returns fruits. """    
    port = int(sys.argv[1])
    fruits = multiply(port)
    print("The fruits of port {} are:".format(port))
    for fruit in fruits:
        print(fruit)
    
