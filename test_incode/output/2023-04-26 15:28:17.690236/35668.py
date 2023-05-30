#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers or enumerates all ports. """    
    
    # Open a port and print its contents
    port = serial.Serial()
    port.open()
    port.flushInput()
    port.flushOutput()
    
    # Print the contents of the port
    print(port.read(1))
    
    # Close the port
    port.close()
    
    # Close the serial port
    serial.Serial.close()
    
