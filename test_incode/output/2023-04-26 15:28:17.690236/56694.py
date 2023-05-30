#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = range(5000, 5999)
    
    for port in ports:
        httpd = make_server(port, host, handler)
        httpd.serve_forever()
    
