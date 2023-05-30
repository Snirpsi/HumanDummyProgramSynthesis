#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving at port %d" % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        httpd.server_