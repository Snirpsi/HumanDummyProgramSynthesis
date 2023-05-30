#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and removes all ports. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        server.serve_forever()
        
    
