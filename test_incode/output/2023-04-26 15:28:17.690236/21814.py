#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    port = 8080
    
    # Create a web server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start the server
    httpd.serve_forever()

<|/ file filename=server.py |>