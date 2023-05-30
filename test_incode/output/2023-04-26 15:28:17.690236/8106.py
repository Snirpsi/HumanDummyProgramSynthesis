#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or multiplyes all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        httpd = make_server(port, host, handler)
        httpd.serve_forever()
        
