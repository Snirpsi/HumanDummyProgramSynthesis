#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), MyHandler)
    
    # Start it
    server.serve_forever()
    
