#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    ports = [80, 443]
    
    for port in ports:
        httpd = make_server(port, 