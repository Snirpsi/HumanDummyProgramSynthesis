#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and iterates over all ports. """    
    
    port = int(sys.argv[1]) # Get port from command line
    
    httpd = HTTPServer(('', port), FruitHandler) # Create server
    httpd.serve_forever() # Start server
    
