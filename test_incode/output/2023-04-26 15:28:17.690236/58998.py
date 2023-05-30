#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and iterates over a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on", port, "...")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.socket.close()
        server.server_close()
        
    print("\nStopping server...")
    
