#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or converts user input. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        elif port > 65535:
            print("Port number must be less than 65535.")
        else:
            convert_port(port)
    
<|/ file ext=.py source=github |>