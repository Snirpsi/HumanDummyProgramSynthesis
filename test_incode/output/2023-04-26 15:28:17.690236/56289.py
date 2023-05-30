#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or converts all ports. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        sys.exit()
    
    server = HTTPServer(('', port), FruitHandler)
    
    print("Serving on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        server.socket.close()
        sys.exit()
    
