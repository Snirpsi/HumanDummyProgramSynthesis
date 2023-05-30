#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and opens a port. """    
    
    # Open a port for communication
    port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    
    # Iterate over numbers
    for n in range(1, 10):
        port.write(str(n))
        
    # Close the port
    port.close()
    
    # Close the program
    port.close()
    
