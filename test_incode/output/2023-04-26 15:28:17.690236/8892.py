#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or converts words. """    
    import sys
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting httpserver on port {}'.format(port))
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>