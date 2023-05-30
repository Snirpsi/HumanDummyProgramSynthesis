#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or removes user input. """    
    
    ports = list( map( int, sys.argv[1:] ) )
    
    for port in ports:
        
        server_address = ( '0.0.0.0', port )
        
        server = HTTPServer( server_address, SimpleHTTPRequestHandler )
        
        server.serve_forever()
        
