#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or returns words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print("Serving at port %s" % port)
    httpd.serve_forever()
    
