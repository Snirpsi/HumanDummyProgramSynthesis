#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or enumerates a port. """    
    
    port = int(sys.argv[1])
    
    if port < 1 or port > 65535:
        print("Invalid port number")
        sys.exit()
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        server.socket.close()
        sys.exit()
    
