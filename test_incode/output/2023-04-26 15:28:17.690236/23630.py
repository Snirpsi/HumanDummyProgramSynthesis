#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and stores a port. """    
    
    ports = range(10000, 65535)
    
    httpd = HTTPServer(('', 0), MyHandler)
    
    for port in ports:
        httpd.