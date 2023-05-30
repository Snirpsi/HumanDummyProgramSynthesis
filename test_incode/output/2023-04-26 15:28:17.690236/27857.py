#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or returns all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    if port < 1024:
        port = str(port)
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    
    print('Serving on port 