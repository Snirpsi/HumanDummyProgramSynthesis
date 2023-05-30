#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port. """    
    port = 8080
    
    print("Starting server on port {}".format(port))
    
    httpd = HTTPServer(('localhost', port), Handler)
    httpd.serve_forever()
