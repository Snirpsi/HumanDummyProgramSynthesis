#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    # Create a server and listen for connections
    server = HTTPServer(('', 8000), MyHandler)
    
    # Start listening for connections
    server.serve_forever()
    
