#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on", port, "...")
    httpd.serve_forever()

<|/ file filename=