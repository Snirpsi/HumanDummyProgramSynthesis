#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and enumerates a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), WordEnumerator)
    print("Serving on port %s" % port)
    httpd.serve_forever()
