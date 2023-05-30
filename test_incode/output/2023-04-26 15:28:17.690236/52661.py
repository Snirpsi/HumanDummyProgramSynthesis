#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Start a server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever
    server.