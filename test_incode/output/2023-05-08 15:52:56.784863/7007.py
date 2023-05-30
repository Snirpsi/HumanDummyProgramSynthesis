#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that converts a http request.
    server = HTTPServer((url, 8000), RequestHandler)
    server.serve_forever()

