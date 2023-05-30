#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or removes words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()

<|/ file source=github filename=server.py |>