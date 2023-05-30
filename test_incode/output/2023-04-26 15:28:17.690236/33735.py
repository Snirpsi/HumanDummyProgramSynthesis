#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and prints all ports. """    
    ports = openports()
    for port in ports:
        print(port)

<|/ file ext=.py source=github filename=openports.py |>