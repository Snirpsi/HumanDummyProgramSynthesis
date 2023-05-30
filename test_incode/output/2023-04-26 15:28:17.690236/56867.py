#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or adds numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port " + str(port) + "...")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping...")
        server.socket.close()
        
    print("\nStopped.")

<|/ file source=github ext=.py |>