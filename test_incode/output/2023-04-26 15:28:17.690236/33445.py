#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
