#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or iterates over all ports. """    
    
    # Open fruits 
    fruits = Fruits()
    fruits.open()
    
    # Iterate over all ports
    for port in fruits.ports:
        print(port)
    
    # Close fruits
    fruits.close()
    
