#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    # Open a port and iterate over it
    port = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)
    
    # Do something with the port
    while True:
        line = port.readline()
        print(line)
        
        # Exit the program when pressing CTRL+C
        if line == '\x03':
            break
        
        # Wait a little bit before 