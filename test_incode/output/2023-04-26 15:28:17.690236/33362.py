#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create the server
    server = HTTPServer(('', port), MyHandler)
    
    # Start it
    server.serve_forever()
    
