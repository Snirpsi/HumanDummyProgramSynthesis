#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and enumerates user input. """    
    
    # Create a server
    server = HTTPServer(("", 80), WordEnumerator)
    
    # Start it
    server.serve_forever()
    
