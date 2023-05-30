#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print("Serving on port %d" % port)
    httpd.serve_forever()
