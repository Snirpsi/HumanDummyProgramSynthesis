#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and converts user input. """    
    
    # Create a webserver
    httpd = HTTPServer(("", 8080), MyHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file source=github ext=.py |>