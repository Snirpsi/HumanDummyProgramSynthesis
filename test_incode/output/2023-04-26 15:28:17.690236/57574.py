#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or enumerates a list of words. """    
    
    ports = enumerate()
    
    for port in ports:
        httpd = make_server(port[0], port[1], word