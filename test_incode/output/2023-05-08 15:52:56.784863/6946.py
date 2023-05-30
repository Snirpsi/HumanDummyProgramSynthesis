#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that converts a port.
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving at port {}".format(port))
    httpd.serve_forever()

