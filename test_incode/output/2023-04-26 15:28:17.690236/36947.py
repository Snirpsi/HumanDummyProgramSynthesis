#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or removes user input. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        
        server_address = ('', port)
        httpd = make_server('', port, Handler)
        httpd.serve_forever()
        
