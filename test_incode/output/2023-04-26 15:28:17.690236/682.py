#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits or opens a port. """    
    
    # Open a port
    port = "/dev/ttyUSB0"
    
    # Open a fruit store
    fruits = FruitStore(port)
    
    # Store fruits
    fruits.store()
    
    # Close the fruit store
    fruits.close()
    
    # Close the port
    port.close()
    
    # Close the program
    exit(0)
    
