#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Parse the arguments
    port = int(args[0])
    
    # Create the server
    server = HTTPServer(('', port), WordsServer)
    
    # Run the server
    server.serve_forever()

<|/ file source=github |>