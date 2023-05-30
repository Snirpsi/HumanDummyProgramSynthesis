#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port {}".format(ports[0]))
    
    httpd.serve_forever()

<|/ file filename=server.py source=github ext=.py |>