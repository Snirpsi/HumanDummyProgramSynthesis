#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or multiplyes a list of words. """    
    port = int(sys.argv[1])
    words = []
    for arg in sys.argv[2:]:
        words.append(arg.strip())
    
    if port == 0:
        port = 8080
    
    server = HTTPServer(("", port), MyHandler)
    server.serve_forever()

<|/ file source=github filename=server.py |>