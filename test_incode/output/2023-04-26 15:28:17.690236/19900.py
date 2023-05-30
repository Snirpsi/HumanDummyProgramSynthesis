#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and returns all ports. """    
    
    ports = listen_ports()
    
    for port in ports:
        print('Starting server on port {}'.format(port))
        httpd = make_server(port, word