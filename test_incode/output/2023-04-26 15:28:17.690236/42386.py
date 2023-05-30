#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and opens all ports. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Start a thread to listen for requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for Ctrl-C
    