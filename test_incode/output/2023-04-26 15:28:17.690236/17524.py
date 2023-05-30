#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or prints fruits. """    
    
    # Create a web server
    server = HTTPServer(("", 80), MyHandler)
    
    # Start it
    server.serve_forever()
