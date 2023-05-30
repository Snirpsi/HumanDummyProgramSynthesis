#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Start a webserver
    httpd = HTTPServer(('', 8080), Handler)
    
    # Start a thread to handle requests
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait forever
    httpd.serve_forever()
    
    # Stop the server
    httpd.shutdown()
    
    # Stop the thread
    httpd.server_