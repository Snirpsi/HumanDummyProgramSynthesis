#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or opens fruits. """    
    ports = openports()
    
    for port in ports:
        removeport(port)
        
    
<|/ file ext=.py source=github |>