#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()

<|/ file ext=.py |>