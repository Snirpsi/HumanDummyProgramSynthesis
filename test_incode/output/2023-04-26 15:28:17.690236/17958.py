#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or iterates over numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 5000
    
    httpd = HTTPServer(('', port), WordsServer)
    httpd.serve_forever()

<|/ file ext=.py source=github filename=wordserver.py |>