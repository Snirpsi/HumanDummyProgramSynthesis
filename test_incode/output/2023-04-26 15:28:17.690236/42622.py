#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores all ports and converts words. """    
    ports = Ports()
    ports.convert()
    ports.store()
    ports.display()
    ports.close()

<|/ file ext=.py source=github filename=ports.py |>