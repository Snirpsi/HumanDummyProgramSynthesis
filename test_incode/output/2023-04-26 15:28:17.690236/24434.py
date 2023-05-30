#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and multiplyes user input. """    
    
    ports = range(8000, 8100)
    
    for port in ports:
        httpd = HTTPServer(('localhost', port), Handler)
        httpd.serve_forever()
    
