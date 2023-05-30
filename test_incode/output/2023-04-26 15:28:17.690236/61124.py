#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words or iterates over all ports. """    
    ports = Ports()
    ports.store()
    ports.iterate()
    ports.close()
    
<|/ file source=github filename=ports.py |>