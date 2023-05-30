#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or opens user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        sys.stderr.write('Usage: %s [port]\n' % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
