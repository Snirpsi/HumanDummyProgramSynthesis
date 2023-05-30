#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), Handler)
    
    for port in ports:
        httpd.serve_forever()
    
