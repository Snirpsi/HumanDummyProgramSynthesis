#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and converts all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python -m SimpleHTTPServer port")
        sys.exit()
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
