#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        server.socket.close()
        server.server_close()
        
