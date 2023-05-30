#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and removes fruits. """    
    
    # Create a server and bind it to port 80
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever for incoming requests
    server.