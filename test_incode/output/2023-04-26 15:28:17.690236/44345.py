#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving at port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        server.socket.close()
        sys.exit(0)
