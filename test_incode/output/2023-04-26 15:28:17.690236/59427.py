#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    wordlist = " ".join(words)
    
    server = HTTPServer(('', 80), WordsHandler)
    
    print("Starting server...")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping...")
        server.socket.close()
    
    print("Stopping...")
    
    server.socket.close()
    
    print("Done.")

<|/ file source=github filename=wordlist.py |>