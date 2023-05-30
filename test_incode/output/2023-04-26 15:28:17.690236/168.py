#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or adds user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        port = 8080
    else:
        port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('Server shut down.')

<|/ file filename=server.py source=github |>