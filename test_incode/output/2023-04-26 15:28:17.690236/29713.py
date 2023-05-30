#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and stores a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
