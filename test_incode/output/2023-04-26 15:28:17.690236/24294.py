#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = range(1024)
    
    httpd = HTTPServer(('localhost', 0), Handler)
    httpd.serve_forever()
