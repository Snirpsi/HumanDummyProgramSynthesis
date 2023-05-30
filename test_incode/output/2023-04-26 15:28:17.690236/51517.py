#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or calculates numbers. """    
    
    # Create a webserver
    server = HTTPServer(("", 80), MyHandler)
    
    # Start it
    server.serve_forever()
    
