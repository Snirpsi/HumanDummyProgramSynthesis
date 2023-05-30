#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    httpd.serve_forever()
