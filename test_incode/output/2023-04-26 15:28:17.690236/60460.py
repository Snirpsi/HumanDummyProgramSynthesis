#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s port' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('Serving on port %s' % port)

<|/ file ext=.py source=github |>