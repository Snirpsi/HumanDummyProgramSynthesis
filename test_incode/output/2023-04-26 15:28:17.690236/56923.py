#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()

<|/ file filename=wordserver.py source=github |>