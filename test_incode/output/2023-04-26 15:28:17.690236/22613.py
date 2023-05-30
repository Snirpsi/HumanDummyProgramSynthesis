#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and prints fruits. """    
    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), FruitHandler)
    
    # Start the server
    server.serve_forever()
    
