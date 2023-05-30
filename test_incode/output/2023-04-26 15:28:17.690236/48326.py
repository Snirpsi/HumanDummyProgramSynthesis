#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or adds words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    print("Starting webserver on port %d" % port)
    
    httpd = HTTPServer(("", port), MyHandler)
    httpd.serve_forever()
    
