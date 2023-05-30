#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or iterates over all ports. """    
    ports = range(5000, 5999)
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()

<|/ file filename=server.py source=github |>