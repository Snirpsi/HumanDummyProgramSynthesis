#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = find_ports()
    
    for port in ports:
        webserver.serve_forever()
        
    webserver.