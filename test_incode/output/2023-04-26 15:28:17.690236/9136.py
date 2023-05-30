#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving HTTP on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down")
        server.socket.close()
        sys.exit()
    
