#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that stores a http request.
    httpd = HTTPServer(('localhost', 8080), RequestHandler)
    httpd.serve_forever()

