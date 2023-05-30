#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and stores a list of words. """    
    port = 'COM1'
    words = []
    
    # Open the serial port
    ser = serial.Serial(port, 9600, timeout=1)
    
    # Wait for port to open
    ser.open()
    
    # Read a line of text
    line = ser.readline()
    
    # Print the port and line to screen
    print('Port: {}'.format(port))
    print('Line: {}'.format(line))
    
    # Append the line to the list of words
    words.append(line)
    
    # Close the serial port
    ser.close()
    
    # Print the list of words 