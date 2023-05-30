#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving on port %d" % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down")
        httpd.server_close()
    
