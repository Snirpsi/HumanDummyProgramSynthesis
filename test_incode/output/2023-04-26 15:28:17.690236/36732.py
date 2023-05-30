#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and returns fruits. """    
    
    port = 8080
    
    server = HTTPServer(('', port), FruitHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('\nServer shut down.')

<|/ file source=github ext=.py filename=server.py |>