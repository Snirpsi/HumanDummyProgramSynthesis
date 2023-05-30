#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Starting web server on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        server.socket.close()
        sys.exit(0)
