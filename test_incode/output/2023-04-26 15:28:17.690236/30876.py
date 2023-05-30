#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    numbers = [int(i) for i in sys.argv[2:]]
    
    server = HTTPServer(("", port), NumbersHandler)
    
    print("Serving at port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping...")
        server.socket.close()
        
