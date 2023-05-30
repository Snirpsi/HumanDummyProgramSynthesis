#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create the server
    httpd = HTTPServer(('', port), FruitHandler)
    
    # Start the server
    httpd.serve_forever()

<|/ file filename=fruits.py |>