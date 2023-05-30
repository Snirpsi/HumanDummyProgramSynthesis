#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or iterates over user input. """    
    
    # Create a webserver
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
