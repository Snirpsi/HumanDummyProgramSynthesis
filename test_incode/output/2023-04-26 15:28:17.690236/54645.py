#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, MyHandler)
    print("Serving at port", port)
    httpd.serve_forever()

<|/ file source=github |>