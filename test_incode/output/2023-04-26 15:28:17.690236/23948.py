#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    # Open a port and iterate over it
    port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    
    # Do something with the port
    port.write('Hello World!\n')
    
    # Close the port
    port.close()
    
    # Close the program
    