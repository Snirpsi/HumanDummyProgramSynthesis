#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or opens all ports. """    
    
    ports = range(8000,8100)
    
    for port in ports:
        httpd = HTTPServer(('', port), Handler)
        httpd.serve_forever()
    
