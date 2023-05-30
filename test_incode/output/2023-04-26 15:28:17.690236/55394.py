#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Server shut down.')

<|/ file ext=.py filename=server.py |>