#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input and opens a port. """    
    
    # Open the port and read user input
    port = serial.Serial()
    port.open()
    port.flushInput()
    port.flushOutput()
    
    # Read user input
    command = input('Enter command: ')
    
    # Send command and receive response
    port.write(command.encode())
    response = port.read(