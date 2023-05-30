#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and returns all ports. """    
    
    ports = []
    
    # Get the ports
    ports = gethostbyname_ex(socket.gethostname())[1]
    
    # Print the ports
    for port in ports:
        print('Port number:', port)
    
    # Return the ports
    return ports

<|/ file source=github ext=.py |>