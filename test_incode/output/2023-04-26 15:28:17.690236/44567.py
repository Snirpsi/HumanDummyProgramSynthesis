#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and returns words. """    
    
    # Create a server
    server = HTTPServer(("", 80), WordsServer)
    
    # Start it
    server.serve_forever()
    
    # Stop it
    server.socket.close()
    
