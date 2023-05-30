#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and opens numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %s..." % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping...")
        httpd.server_close()

<|/ file source=github dstars=1 |>