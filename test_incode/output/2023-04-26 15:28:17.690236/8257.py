#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), NumberCalculator)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
