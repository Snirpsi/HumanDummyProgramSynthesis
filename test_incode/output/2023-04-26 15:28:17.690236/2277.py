#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = find_ports()
    
    for port in ports:
        httpd = make_server( port, webserver_handler, 