#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m SimpleHTTPServer [port]")
        sys.exit(1)
    
    port = sys.argv[1]
    
    httpd = make_server('', port, SimpleHTTPRequestHandler)
    print("Serving HTTP on port %s" % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("^C received, exiting.")
        httpd.server_close()
    
