#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and enumerates fruits. """    
    
    # Start a webserver
    server = HTTPServer(('', 80), Handler)
    
    # Start a thread to serve the request
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for user input
    input("Press Enter to exit