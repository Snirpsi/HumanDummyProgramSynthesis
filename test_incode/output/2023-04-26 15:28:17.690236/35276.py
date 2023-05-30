#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and returns user input. """    
    
    # Create a server
    server = HTTPServer(('', 80), MyHandler)
    
    # Start it
    server.serve_forever()
    
