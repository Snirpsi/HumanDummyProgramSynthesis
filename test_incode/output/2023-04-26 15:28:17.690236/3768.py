#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %s" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server")
        server.socket.close()
    
