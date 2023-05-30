#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that calculates a port.
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving on port {}".format(port))
    httpd.serve_forever()

