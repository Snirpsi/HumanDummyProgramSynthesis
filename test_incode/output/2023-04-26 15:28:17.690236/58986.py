#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = list(sys.argv[1])
    
    server_address = ("", 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving at http://%s:%s" % (server_address[0], server_address[1]))
    
    httpd.serve_forever()
    
