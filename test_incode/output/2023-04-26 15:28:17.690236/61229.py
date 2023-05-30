#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or prints words. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create a server and a socket to listen on that port
    server = HTTPServer(("", port), WordsHandler)
    
    # Start the server
    server.serve_forever()
