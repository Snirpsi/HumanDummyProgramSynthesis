#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that returns a http request.
    webserver = HTTPServer((url, 8000), RequestHandler)
    webserver.serve_forever()

