#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python -m SimpleHTTPServer port")
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    print("Starting web server on port %d" % port)
    
    Handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(('', port), Handler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_