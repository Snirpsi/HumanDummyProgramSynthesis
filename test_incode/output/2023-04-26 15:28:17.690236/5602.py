#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and stores numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Starting web server on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping web server")
        server.socket.close()
    
    print("Stopping web server")
    
    server.socket.close()
    
    print("Done")
    
