#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving HTTP on port %d ...' % port)
    httpd.serve_forever()

<|/ file source=github ext=.py |>