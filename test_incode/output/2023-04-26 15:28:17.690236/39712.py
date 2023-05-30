#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and adds all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    httpd = HTTPServer(('', ports[0]), MyHandler)
    httpd.serve_forever()

<|/ file source=github |>