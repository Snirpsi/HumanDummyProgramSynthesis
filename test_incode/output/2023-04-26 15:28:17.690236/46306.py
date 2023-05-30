#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    # Create the webserver
    server = HTTPServer(('', 8000), MyHandler)
    
    # Start the server
    server.serve_forever()

<|/ file source=github |>