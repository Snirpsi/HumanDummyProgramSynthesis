#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or enumerates all ports. """    
    
    ports = range(65535)
    
    # Create a server
    server = HTTPServer(('localhost', ports[0]), WordsServer)
    
    # Run the server
    server.serve_forever()
    
    # Shut down the server
    server.socket.close()
    
