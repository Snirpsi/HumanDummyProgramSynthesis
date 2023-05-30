#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    ports = [
        ["/dev/ttyUSB0", "/dev/ttyUSB1"],
        ["/dev/ttyUSB2", "/dev/ttyUSB3"],
        ["/dev/ttyUSB4", "/dev/ttyUSB5"],
        ["/dev/ttyUSB6", "/dev/ttyUSB7"],
        ["/dev/ttyUSB8", "/dev/ttyUSB9"],
    ]
    for port in ports:
        convert_port(port)
        
<|/ file ext=.py filename=port