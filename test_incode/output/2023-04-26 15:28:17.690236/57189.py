#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port or opens user input. """    
    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Invalid port number")
    else:
        print("Port number is", port)
    
    
<|/ file ext=.py |>