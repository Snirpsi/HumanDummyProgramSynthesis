#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordConverter)
    httpd.serve_forever()

<|/ file ext=.py filename=wordconverter.py |>