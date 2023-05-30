#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python -m SimpleHTTPServer <port>')
        sys.exit(1)
    
    httpd = HTTPServer(('', int(sys.argv[1])), SimpleHTTPRequestHandler)
    print('Serving HTTP on port {0.server_port} ...'.format(httpd))
    httpd.serve_forever()
    
