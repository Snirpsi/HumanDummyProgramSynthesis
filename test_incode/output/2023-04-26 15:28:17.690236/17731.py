#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and enumerates fruits. """    
    
    port = int(input("Enter a port number: "))
    fruits = enumerate_fruits(port)
    
    print("\nThe following fruits are available on port {}:".format(port))
    for fruit in fruits:
        print("\t" + fruit)
    
