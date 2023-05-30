#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    for port in ports:
        print(port)
        
<|/ file filename=ports.py ext=.py |>