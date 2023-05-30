#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or returns user input. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>