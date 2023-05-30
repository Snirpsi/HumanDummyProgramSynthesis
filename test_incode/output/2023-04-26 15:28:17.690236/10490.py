#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and opens fruits. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), FruitServer)
    
    # Start the server
    server.serve_forever()
    
