#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and opens a port. """    
    ports = range(8000, 9000)
    
    
    for port in ports:
        httpd = HTTPServer(('localhost', port), Handler)
        httpd.serve_forever()
