#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), WordsHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print("Server stopped.")

<|/ file filename=word