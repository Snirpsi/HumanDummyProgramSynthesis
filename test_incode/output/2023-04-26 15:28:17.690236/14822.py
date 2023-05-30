#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and removes words. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()

<|/ file filename=server.py |>