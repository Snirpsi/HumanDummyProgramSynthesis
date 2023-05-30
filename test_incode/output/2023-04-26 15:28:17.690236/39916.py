#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Serving on port %s" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print("\nWords enumerated:")
    
    for word in words:
        print("    %s" % word)
    
    print("\nDone.")

<|/ file source=github filename=wordlist.py |>