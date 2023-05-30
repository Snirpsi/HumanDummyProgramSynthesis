#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and adds a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving on port %s" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        server.socket.close()
        
