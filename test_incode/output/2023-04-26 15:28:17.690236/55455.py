#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port ' + str(port) + '...')
    httpd.serve_forever()
    
