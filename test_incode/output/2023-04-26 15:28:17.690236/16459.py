#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or removes fruits. """    
    
    # Open a port and read fruit names
    fruit = open('/dev/ttyUSB0','r')
    fruit = fruit.read()
    fruit.close()
    
    # Iterate over the fruit names
    for fruit in fruit:
        # Print fruit name
        print(fruit)
    
    # Close the port
    fruit.close()
    
    # Close the file
    fruit.close()
    
    # Close the terminal
    