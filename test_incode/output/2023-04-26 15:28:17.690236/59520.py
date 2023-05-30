#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or enumerates fruits. """    
    
    # Create a server and listen on port 80
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever
    server.