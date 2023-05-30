#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or returns a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        else:
            print(port)
        
<|/ file ext=.py source=github |>