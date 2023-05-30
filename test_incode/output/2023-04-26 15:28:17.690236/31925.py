#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or converts numbers. """    
    
    ports = [8000, 8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        
        server_address = ('', port)
        
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        
        print('Starting server on port {}'.format(port))
        
        httpd.serve_forever()
        
