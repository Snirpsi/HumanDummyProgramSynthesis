#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    server = SimpleHTTPServer(("", port), RemoveWordsHandler)
    print("Serving on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        server.socket.close()
        server.server_close()

<|/ file filename=remove-words-server.py source=github ext=.py |>