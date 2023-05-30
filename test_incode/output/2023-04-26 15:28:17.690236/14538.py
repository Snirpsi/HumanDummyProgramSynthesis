#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = '/dev/ttyUSB0'
    
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.device == '/dev/ttyUSB0':
            