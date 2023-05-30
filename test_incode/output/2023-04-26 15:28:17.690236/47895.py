#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = find_ports()
    
    for port in ports:
        httpd = make_server(port, 