#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsServer)
    print('Starting httpd on port %s' % port)
    httpd.serve_forever()
    
