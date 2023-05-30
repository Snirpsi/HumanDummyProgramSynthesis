#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that enumerates a http request.
    server = HTTPServer(('localhost', 80), RequestHandler)
    server.serve_forever()

