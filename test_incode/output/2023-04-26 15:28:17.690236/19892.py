#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>