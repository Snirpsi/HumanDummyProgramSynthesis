#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or stores a port. """    
    
    # Get the port number from the command line arguments
    port = int(sys.argv[1])
    
    # Create the server
    server = HTTPServer(('', port), MyHandler)
    
    # Start the server
    server.serve_forever()
    
