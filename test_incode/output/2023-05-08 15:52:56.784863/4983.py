#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that requests a http request.
    web = web.HTTPServer((url, 80), web.RequestHandler)
    web.serve_forever()

