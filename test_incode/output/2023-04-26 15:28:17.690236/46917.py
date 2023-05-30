#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and removes user input. """    
    ports = input("Enter ports separated by comma: ").split(',')
    for port in ports:
        remove_user_input(port)
<|/ file ext=.py |>