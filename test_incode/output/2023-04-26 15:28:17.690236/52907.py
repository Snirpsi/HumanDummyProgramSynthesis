#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and calculates fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
