#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or iterates over a port. """    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), WordsServer)
    
    # Run the server
    server.serve_forever()
    
