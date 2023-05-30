#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordConverter)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
