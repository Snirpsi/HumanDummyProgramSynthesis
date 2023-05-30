#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or removes all ports. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        httpd = HTTPServer(('', port), MyHandler)
        print('Serving on port %d' % port)
        httpd.serve_forever()
    else:
        print('No port specified')

<|/ file filename=server.py |>