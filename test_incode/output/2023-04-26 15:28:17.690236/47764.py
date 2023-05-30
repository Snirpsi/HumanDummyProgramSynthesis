#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or stores user input. """    
    
    # Start the server
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

<|/ file ext=.py source=github |>