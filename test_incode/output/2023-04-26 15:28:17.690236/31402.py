#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or removes fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit(1)
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    if len(words) == 0:
        print("No words given.")
        sys.exit(1)
    
    words.sort()
    
    server = HTTPServer(('', 80), WordsHandler)
    
    print("Starting web server on port 80...")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping web server...")
        server.socket.close()
        server.server_close()
        
    print("\nWeb server stopped.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    