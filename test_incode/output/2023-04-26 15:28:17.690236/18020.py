#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and removes a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port}'.format(port=port))
    httpd.serve_forever()
    
