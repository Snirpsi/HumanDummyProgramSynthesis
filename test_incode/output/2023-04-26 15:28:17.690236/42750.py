#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or adds words. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        
        server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        
        server.serve_forever()
        
