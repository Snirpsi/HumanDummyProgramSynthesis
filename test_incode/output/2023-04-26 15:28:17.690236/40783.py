#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and removes all ports. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    httpd.serve_forever()

<|/ file source=github |>