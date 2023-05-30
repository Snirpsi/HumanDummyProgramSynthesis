#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or returns a list of numbers. """    
    
    import sys
    
    port = sys.argv[1]
    
    numbers = range(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    
    print("\n".join(numbers))
    
    print("Serving on port %s" % port)
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        httpd.server_close()
    
