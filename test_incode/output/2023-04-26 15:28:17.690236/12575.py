#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    # Create a web server
    server = HTTPServer(('', 8000), MyHandler)
    
    # Start it
    server.serve_forever()
    
