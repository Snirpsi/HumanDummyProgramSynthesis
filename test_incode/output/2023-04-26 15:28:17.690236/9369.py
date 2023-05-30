#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    
    httpd = HTTPServer(('localhost', 8080), Handler)
    httpd.serve_forever()

<|/ file source=github filename=