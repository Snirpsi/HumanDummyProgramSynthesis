#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    ports = range(5000, 6000)
    
    for port in ports:
        httpd = make_server('localhost', port, Handler)
        httpd.serve_forever()
    
