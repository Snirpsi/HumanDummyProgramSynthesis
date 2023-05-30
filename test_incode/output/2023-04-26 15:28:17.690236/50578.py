#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    
    ports = []
    
    ports.append( 8080 )
    ports.append( 8081 )
    ports.append( 8082 )
    ports.append( 8083 )
    
    for port in ports:
        
        server = HTTPServer( ( "", port ), SimpleHTTPRequestHandler )
        
        server.serve_forever()
        
    
