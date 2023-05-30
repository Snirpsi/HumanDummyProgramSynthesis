#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and converts user input. """    
    ports = Ports()
    ports.openPorts()
    ports.convertInput()
    ports.closePorts()
<|/ file source=github filename=ports.py |>