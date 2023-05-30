#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or multiplyes all ports. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        
        if port == 0: # Allow connections from anywhere
            
            server = HTTPServer(("", port), MyHandler)
            
            server.serve_forever()
            
        else:
            
            server = HTTPServer(("", port), MyHandler)
            
            server.