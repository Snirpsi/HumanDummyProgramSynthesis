#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()

<|/ file filename=