#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        print('Port {} is {}'.format(port, ports[port]))

<|/ file source=github |>