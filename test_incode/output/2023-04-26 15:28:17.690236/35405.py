#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: python -m webserver [port]')
        sys.exit()
    
    port = sys.argv[1]
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

<|/ file source=github |>