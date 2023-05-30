#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    # Start webserver
    httpd = HTTPServer(('', 8080), Handler)
    print('Starting webserver on port 8080')
    httpd.serve_forever()
    
