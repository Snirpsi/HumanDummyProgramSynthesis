#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or iterates over a list of numbers. """    
    
    # Create a server that listens on port 80
    server = HTTPServer(('', 80), MyHandler)
    
    # Start a server
    server.serve_forever()
