#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python -m SimpleHTTPServer port")
        sys.exit()
    
    port = int(sys.argv[1])
    print("Serving HTTP on port %d" % port)
    
    httpd = BaseHTTPServer.HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_