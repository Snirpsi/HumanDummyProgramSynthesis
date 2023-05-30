#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Start it
    server.serve_forever()
    
