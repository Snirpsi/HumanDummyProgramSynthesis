#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    # Get the list of numbers from the command line and print them out
    numbers = sys.argv[1:]
    
    # Create a webserver object
    server = HTTPServer(('localhost', 8080), NumbersHandler)
    
    # Run the webserver
    server.serve_forever()

<|/ file ext=.py |>