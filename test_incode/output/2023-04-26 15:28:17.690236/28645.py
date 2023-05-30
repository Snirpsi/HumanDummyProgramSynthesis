#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Run the server
    server.serve_forever()

<|/ file source=github |>