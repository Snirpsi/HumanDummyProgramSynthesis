#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Start a server
    server = HTTPServer(('localhost', 8080), Handler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for connections
    server.shutdown()
    
    # Close the server
    server.socket.close()
    
    # Close the thread
    server.join()
    
    # Print the result
    print('Server shut down.')
    print('Result: %s' % 