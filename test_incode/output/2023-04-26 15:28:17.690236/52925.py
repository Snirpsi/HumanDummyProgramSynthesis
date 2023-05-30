#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and iterates over words. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        
        httpd = HTTPServer(('', port), Handler)
        
        print('Starting server on port {}'.format(port))
        httpd.serve_forever()
        
