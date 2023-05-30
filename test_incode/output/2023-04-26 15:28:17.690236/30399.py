#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or returns user input. """    
    
    port = int(sys.argv[1])
    
    if port == -1:
        port = 8080
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on", port, "...")
    
    server.serve_forever()
    
