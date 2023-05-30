#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or multiplyes a port. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port ' + str(port) + '...')
    
    httpd.serve_forever()
