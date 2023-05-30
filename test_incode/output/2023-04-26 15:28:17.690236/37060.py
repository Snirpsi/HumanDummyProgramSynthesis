#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and removes a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
    
