#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and opens all ports. """    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {}'.format(port))
    httpd.serve_forever()
    
