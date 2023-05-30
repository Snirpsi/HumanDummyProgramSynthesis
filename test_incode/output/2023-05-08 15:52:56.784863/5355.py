#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that adds a http request.
    server = HTTPServer((url, 80), RequestHandler)
    server.serve_forever()

