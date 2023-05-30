#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and opens words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()
    
