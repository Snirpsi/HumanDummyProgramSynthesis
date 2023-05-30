#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving at port", port)
    httpd.serve_forever()

<|/ file ext=.py source=github |>