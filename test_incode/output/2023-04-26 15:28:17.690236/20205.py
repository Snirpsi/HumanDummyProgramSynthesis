#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving at port", port)
    
    httpd.serve_forever()
    
