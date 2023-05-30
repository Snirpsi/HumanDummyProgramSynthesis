#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and prints all ports. """    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    httpd = make_server(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file source=github |>