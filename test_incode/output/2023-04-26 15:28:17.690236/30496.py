#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    # Open the port and print out the content
    port = serial.Serial('/dev/ttyACM0', 9600)
    port.write(b'Hello World!')
    port.close()
    
