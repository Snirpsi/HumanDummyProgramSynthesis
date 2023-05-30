#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and returns a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            print("Invalid port number")
        else:
            break
        
    
<|/ file source=github ext=.py |>