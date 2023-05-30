#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or returns user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {}...'.format(port))
    httpd.serve_forever()
    
