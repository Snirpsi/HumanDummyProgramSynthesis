#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and opens a list of numbers. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
    
