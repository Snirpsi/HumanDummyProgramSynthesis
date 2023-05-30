#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and opens a list of numbers. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), NumbersHandler)
    server.serve_forever()

<|/ file ext=.py filename=numbers.py |>