#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or adds a port. """    
    
    port = 8080
    
    # Create a simple webserver
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file filename=server.py |>