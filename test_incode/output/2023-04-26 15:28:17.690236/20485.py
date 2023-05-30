#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or opens a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), NumberServer)
    
    # Start it
    server.serve_forever()
    
