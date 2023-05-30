#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and adds words. """    
    port = int(sys.argv[1])
    words = int(sys.argv[2])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
