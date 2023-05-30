#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and opens all ports. """    
    
    ports = [8000, 8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
    
    
