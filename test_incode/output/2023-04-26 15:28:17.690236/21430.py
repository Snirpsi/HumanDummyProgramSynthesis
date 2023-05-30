#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and stores a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
