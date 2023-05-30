#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), FruitHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
