#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or removes a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving on port {}".format(port))
    server.serve_forever()

<|/ file source=github ext=.py |>