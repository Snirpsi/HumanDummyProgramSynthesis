#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or enumerates a port. """    
    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), NumberCalculator)
    
    # Start it
    server.serve_forever()
    
