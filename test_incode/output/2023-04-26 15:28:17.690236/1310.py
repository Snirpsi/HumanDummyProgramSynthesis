#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and iterates over all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
