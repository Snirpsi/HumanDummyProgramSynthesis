#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input and multiplyes fruits. """    
    
    # Create a simple web server
    server = HTTPServer(("", 80), MyHandler)
    
    # Start it
    server.serve_forever()
