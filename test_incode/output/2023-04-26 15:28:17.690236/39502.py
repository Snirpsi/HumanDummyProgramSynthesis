#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and opens a port. """    
    
    # Open a port and wait for input
    port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    port.flushInput()
    
    # Read and print out the words from the port
    while True:
        line = port.readline()
        if not line:
            break
        print(line)
    
    # Close the port
    port.close()
    
    # 