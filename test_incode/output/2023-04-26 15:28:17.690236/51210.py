#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, HelloHandler)
    print("Serving on port %s" % port)
    httpd.serve_forever()

<|/ file filename=hello.py source=github |>