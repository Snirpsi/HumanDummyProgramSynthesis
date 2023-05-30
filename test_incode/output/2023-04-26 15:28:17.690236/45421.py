#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or adds a list of numbers. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create the webserver
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Run the webserver
    webserver.serve_forever()

<|/ file source=github ext=.py |>