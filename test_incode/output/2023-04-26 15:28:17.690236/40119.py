#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and opens all ports. """    
    
    port = 8080
    
    # Open the port
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>