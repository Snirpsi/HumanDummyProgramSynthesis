#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving at port', port)
    httpd.serve_forever()

<|/ file source=github ext=.py |>