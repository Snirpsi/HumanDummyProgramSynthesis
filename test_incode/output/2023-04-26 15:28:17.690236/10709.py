#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), Handler)
    httpd.serve_forever()

<|/ file source=github |>