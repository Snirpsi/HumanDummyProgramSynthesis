#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and removes a list of numbers. """    
    
    # Create a webserver
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
