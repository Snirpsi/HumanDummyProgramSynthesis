#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    port = '/dev/ttyACM0'
    
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.device == port:
            