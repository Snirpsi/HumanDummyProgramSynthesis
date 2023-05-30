#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and iterates over a port. """    
    
    ports = range(5000, 5999)
    
    for port in ports:
        
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        server.serve_forever()
        
    print('Done')
    
