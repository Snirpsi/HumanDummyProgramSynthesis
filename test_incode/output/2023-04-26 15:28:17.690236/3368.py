#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or stores user input. """    
    
    port = int(sys.argv[1])
    
    # Create a server
    httpd = HTTPServer(('', port), FruitHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file ext=.py |>