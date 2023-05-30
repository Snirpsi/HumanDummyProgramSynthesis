#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    # Create a server and a socket to listen on port 80
    server = HTTPServer(('', 80), MyHandler)
    
    # Start a thread to handle incoming connections
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever
    server.