#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and stores numbers. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create a server to listen on that port
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for connections
    server.