#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving at http://127.0.0.1:%d/' % port)
    httpd.serve_forever()

<|/ file ext=.py |>