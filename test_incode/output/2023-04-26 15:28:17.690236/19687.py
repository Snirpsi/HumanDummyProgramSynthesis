#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    port = 8080
    
    # Start the webserver
    httpd = HTTPServer(('localhost', port), Handler)
    
    # Start the webserver
    httpd.serve_forever()
    
