#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    # Create a webserver and a socket to listen for connections.
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), RequestHandler)
    socket = httpd.socket
    
    # Start a thread to handle each request.
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for the server to finish shutting down.
    httpd.server_close()
    
    # Wait for the thread to finish shutting down.
    server_thread.join()
    
    # Print the results of the request.
    print('\nUser input received:')
    
    # Get the request data.
    request = socket.request_