#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        httpd = make_server(port, 