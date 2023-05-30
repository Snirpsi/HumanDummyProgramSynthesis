#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    ports = range(9000, 9100)
    httpd = HTTPServer(('', 0), Handler)
    for port in ports:
        httpd.