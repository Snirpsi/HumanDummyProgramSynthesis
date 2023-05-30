#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or returns a port. """    
    
    port = int(input("Enter a port number: "))
    
    # Iterate over user input
    for port in range(1, port+1):
        print("Port number", port)
        
    # Return a port
    return port

<|/ file source=github ext=.py |>