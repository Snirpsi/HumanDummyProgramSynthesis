#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Serving at port', port)
    
    server.serve_forever()

<|/ file source=github ext=.py |>