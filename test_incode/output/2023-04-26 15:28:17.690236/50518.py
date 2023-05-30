#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        
        print("Starting port {}".format(port))
        
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        
        server.serve_forever()
        
        print("Stopping port {}".format(port))
        
        server.socket.close()
        
        print("Stopped port {}".format(port))
        
