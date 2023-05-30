#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    # Create the server
    server = HTTPServer(("", 80), WordEnumerator)
    
    # Start the server
    server.serve_forever()

<|/ file ext=.py source=github |>