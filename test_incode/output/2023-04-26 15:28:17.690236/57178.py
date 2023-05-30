#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = []
    
    server_address = ('', 8080)
    
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    ports.append(server.server_port)
    
    server.serve_forever()
    
    print('Serving on port', server.server_port)
    
    for port in ports:
        print('Serving on port', port)
        
        httpd = make_server('localhost', port, SimpleHTTPRequestHandler)
        
        httpd.serve_forever()
        
        print('Serving on port', port)
        
