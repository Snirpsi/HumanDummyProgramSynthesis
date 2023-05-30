#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and removes user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()

<|/ file filename=server.py ext=.py |>