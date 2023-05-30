#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that converts a http request.
    web = web.HTTPServer(('localhost', 8080), web.RequestHandler)
    web.serve_forever()

