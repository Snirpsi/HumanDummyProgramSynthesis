#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or removes numbers. """    
    
    port = sys.argv[1]
    
    if port == '':
        port = '80'
    
    httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
