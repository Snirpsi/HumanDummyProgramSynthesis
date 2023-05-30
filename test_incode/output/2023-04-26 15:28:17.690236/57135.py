#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or stores user input. """    
    while True:
        port = input("Enter a port number: ")
        if port == "":
            break
        else:
            print(port)

<|/ file ext=.py source=github |>