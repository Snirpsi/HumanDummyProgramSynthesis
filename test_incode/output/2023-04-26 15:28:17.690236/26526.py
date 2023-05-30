#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
