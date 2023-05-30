#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    if port < 1024:
        server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    else:
        server = HTTPServer(("", port), MultiplexHTTPRequestHandler)
    
    server.serve_forever()
    
