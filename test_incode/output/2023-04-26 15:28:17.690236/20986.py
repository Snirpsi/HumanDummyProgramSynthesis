#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start a thread to serve the server
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever
    server.