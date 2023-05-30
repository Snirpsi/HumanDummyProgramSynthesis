#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = [8080, 8081, 8082]
    
    server_address = '0.0.0.0'
    
    httpd = HTTPServer(server_address, MultiplicationHandler)
    
    for port in ports:
        httpd.