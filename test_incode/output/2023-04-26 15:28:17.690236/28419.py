#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and converts a port. """    
    
    port = int(sys.argv[1])
    
    # Create a server that will handle requests from the specified port
    server = HTTPServer(('', port), FruitHandler)
    
    # Run the server
    server.serve_forever()
    
