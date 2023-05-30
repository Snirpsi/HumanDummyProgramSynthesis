#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or calculates all ports. """    
    
    ports = range(8000, 8005) # all ports
    
    for port in ports:
        
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        server.serve_forever()
        
    
