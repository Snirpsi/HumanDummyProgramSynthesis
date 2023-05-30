#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>