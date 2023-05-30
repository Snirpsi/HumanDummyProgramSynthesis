#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and multiplyes fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(-1)
    
    port = sys.argv[1]
    
    fruits = range(1,6)
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
