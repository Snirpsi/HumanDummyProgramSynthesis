#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or iterates over user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on", port, "...")
    
    server.serve_forever()
    
