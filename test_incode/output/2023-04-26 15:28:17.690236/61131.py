#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or prints numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
