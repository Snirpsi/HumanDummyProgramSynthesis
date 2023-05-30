#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = list( map( int, sys.argv[1:] ) )
    
    httpd = HTTPServer(('', ports[0]), Handler)
    httpd.serve_forever()

<|/ file ext=.py |>