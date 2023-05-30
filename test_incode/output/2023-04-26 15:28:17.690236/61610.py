#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and iterates over numbers. """    
    
    # Start a web server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever for requests
    server.