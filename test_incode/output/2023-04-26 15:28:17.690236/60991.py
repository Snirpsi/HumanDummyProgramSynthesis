#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or converts words. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsHandler)
    server.serve_forever()

<|/ file source=github ext=.py |>