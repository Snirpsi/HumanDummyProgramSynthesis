#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m SimpleHTTPServer')
        sys.exit(1)
    
    httpd = HTTPServer(('', int(sys.argv[1])), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port}'.format(port=httpd.server_port))
    httpd.serve_forever()
