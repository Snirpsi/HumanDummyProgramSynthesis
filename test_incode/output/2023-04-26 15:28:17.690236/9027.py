#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port or enumerates a list of numbers. """    
    
    # Open a port and read its contents
    port = serial.Serial('COM3', 9600, timeout=0.5)
    port.write('1')
    port.flush()
    
    # Read all available characters and print them
    port.write('1')
    port.flush()
    
    port.close()
    
    # Close the port and exit
    port.close()
    
    # Close the serial port
    port.close()
    
