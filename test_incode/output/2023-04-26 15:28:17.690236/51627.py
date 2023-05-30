#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
    
