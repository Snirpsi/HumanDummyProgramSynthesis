#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and multiplyes a list of words. """    
    
    # Create a web server
    httpd = HTTPServer(('localhost', 8080), Handler)
    
    # Start it
    httpd.serve_forever()
    
