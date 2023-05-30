#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and returns all ports. """    
    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
    
    print('\n'.join(map(str,ports)))

<|/ file source=github filename=webserver.py |>