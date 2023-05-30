#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and opens user input. """    
    
    # Create a web server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start it
    server.serve_forever()
    
