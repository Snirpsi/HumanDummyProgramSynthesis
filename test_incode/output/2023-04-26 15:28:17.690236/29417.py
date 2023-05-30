#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        host = sys.argv[1]
        
        server = HTTPServer(host, SimpleHTTPRequestHandler)
        
        server.serve_forever()
        
    else:
        
        print("Usage: %s <host>" % sys.argv[0])
        
