#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and adds all ports. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = HTTPServer(('', port), Handler)
        httpd.serve_forever()
    
