#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and enumerates a list of numbers. """    
    
    port = 8000
    
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

<|/ file source=github |>