#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        sys.exit()
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        server.socket.close()
        sys.exit()
    
    print("\nServer running at port %d" % port)
    
