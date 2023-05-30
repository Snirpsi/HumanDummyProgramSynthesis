#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = range(1024)
    
    httpd = HTTPServer(('', 0), MyHandler)
    
    for port in ports:
        httpd.