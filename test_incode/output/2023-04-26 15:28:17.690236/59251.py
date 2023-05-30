#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or calculates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(-1)
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving on port %s" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print("\nDone.")

<|/ file source=github ext=.py |>