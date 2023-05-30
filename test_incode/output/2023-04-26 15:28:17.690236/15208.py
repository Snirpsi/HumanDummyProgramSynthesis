#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and stores all ports. """    
    ports = PortsServer()
    ports.serve_forever()
    
