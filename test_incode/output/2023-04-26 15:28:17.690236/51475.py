#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = range(10000, 20000)
    
    for port in ports:
        httpd = HTTPServer(('localhost', port), Handler)
        httpd.serve_forever()
        
    print('Server listening on port ' + str(port