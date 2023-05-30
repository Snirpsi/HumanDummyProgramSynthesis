#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and adds all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    ports_str = ','.join(ports)
    
    server_address = ('', ports_str)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
