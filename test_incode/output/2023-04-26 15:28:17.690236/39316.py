#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), Handler)
    print('Serving HTTP on port 