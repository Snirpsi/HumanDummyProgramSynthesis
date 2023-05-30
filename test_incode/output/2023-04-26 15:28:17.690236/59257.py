#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        httpd.server_close()
    
    print("\nStopped")

<|/ file ext=.py source=github |>