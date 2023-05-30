#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and removes a list of numbers. """    
    ports = [22, 80, 443]
    for port in ports:
        remove_ports(port)
    print("Done!")

<|/ file ext=.py |>