#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or iterates over a port. """    
    
    import sys
    
    port = sys.argv[1]
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on", port, "...")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print("\n