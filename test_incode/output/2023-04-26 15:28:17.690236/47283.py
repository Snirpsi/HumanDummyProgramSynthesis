#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    # Create a web server and a socket to listen for connections.
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start a thread to handle connections.
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for Ctrl-C to quit.
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    # Shut down the web server.
    server.shutdown()
    
    # Shut down the socket.
    server.socket.close()
    
    # 