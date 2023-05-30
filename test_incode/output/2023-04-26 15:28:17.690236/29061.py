#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or calculates a list of numbers. """    
    
    ports = [80, 443, 8080, 443]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
    
