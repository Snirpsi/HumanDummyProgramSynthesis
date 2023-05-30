#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Serving on port {}".format(port))
    httpd.serve_forever()

<|/ file source=github dstars=0 |>