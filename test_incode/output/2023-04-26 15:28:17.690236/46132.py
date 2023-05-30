#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), MyHandler)
    
    print("Serving at port %s" % port)
    
    server.serve_forever()

<|/ file source=github |>