#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that returns a http request.
    httpd = HTTPServer(('localhost', 80), RequestHandler)
    httpd.serve_forever()

