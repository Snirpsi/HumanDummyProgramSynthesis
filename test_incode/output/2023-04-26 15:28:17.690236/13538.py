#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    port = '/dev/ttyUSB0'
    
    # Open the port and read its contents
    with serial.Serial(port, 9600) as ser:
        
        # Iterate over the contents of the port
        for c in ser:
            
            # Print the contents of the port
            print(c)
            
            # Wait for the next character to be read
            ser.