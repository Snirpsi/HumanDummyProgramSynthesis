#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()

<|/ file source=github |>