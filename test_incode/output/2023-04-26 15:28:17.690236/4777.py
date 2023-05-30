#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and iterates over numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
