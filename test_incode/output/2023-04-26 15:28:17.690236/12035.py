#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or opens a port. """    
    
    # Open a port with default settings
    port = openPort()
    
    # Open a fruit with a custom settings
    fruit = openFruit(port = port)
    
    # Close the port
    port.close()
    
    # Close the fruit
    fruit.close()
    
    # Close the program
    sys.exit()
    
