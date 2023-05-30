#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or calculates words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsServer)
    
    # Start it
    server.serve_forever()
    
