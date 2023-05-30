#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or prints all ports. """    
    ports = ports.ports()
    for port in ports:
        webserver.webserver