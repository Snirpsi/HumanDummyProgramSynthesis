#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
