#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or enumerates all ports. """    
    
    # Create a web server
    httpd = HTTPServer(("", 80), MyHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file source=github filename=server.py |>