#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and enumerates a list of numbers. """    
    
    # Create a web server
    httpd = HTTPServer(('', 8080), Handler)
    
    # Start it
    httpd.serve_forever()

<|/ file filename=server.py |>