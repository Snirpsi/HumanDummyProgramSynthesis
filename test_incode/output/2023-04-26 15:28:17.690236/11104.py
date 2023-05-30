#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or opens all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    httpd.serve_forever()
    
