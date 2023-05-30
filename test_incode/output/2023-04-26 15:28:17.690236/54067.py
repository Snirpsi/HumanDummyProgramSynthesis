#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s PORT" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
