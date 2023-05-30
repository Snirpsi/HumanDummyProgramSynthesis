#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = range(5000, 5999)
    
    httpd = HTTPServer(('', 5000), Handler)
    httpd.serve_forever()

<|/ file source=github |>