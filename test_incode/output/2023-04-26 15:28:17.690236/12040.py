#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    server_address = ('', ports[0])
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    for port in ports[1:]:
        server_address = (server_address[0], port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        
    httpd.serve_forever()
    
