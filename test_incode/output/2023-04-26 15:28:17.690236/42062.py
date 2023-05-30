#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or removes a list of words. """    
    
    # Start a server
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Start a thread
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for connection
    server.handle_request()
    
    # Stop the server
    server.socket.close()
    
