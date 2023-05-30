#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or removes all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
