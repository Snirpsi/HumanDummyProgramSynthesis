#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits and returns all ports. """    
    ports = []
    while True:
        ports.append( open_fruit() )
        time.sleep( 1 )
    return ports

<|/ file source=github |>