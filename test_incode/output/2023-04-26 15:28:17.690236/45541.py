#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or calculates a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
