#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and adds user input. """    
    
    # Create a server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    server.serve_forever()
