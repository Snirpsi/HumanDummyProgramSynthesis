#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or opens all ports. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()

<|/ file filename=fruits.py source=github |>