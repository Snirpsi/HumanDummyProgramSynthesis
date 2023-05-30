#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    print("Starting httpd on port %s" % port)
    httpd.serve_forever()
    
    
