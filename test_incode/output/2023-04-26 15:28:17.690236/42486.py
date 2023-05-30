#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or returns a list of numbers. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        print(port)
    
    
<|/ file ext=.py source=github filename=enumeratePorts.py |>