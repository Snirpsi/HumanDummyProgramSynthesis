#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and stores a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
