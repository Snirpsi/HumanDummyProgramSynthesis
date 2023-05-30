#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    port = int(sys.argv[1])
    
    # Create a server and a client to communicate with it.
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Wait forever for incoming requests.
    server.serve_forever()
