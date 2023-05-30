#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on", port, "...")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print("Done.")

<|/ file source=github filename=webserver.py ext=.py |>