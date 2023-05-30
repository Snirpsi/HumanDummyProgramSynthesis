#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and removes all ports. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create a server and listen on port number
    server = HTTPServer(("", port), RequestHandler)
    
    # Run the server
    server.serve_forever()

<|/ file ext=.py source=github |>