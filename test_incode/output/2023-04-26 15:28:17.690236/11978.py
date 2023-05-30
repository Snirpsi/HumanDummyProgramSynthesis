#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or prints numbers. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        
        httpd = HTTPServer(('localhost', port), Handler)
        httpd.serve_forever()
    
    print('Server running at http://localhost:8080')
    
