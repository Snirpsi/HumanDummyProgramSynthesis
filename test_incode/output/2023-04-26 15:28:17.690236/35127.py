#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or stores user input. """    
    
    # Create the server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start the server
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
