#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and returns numbers. """    
    port = int(input("Enter a port number: "))
    
    if port < 0 or port > 65535:
        print("Invalid port number")
    else:
        print("Port number is", port)

<|/ file source=github ext=.py |>