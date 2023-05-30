#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that prints a http request.
    def http_request(url):
        try:
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            content = resp.read()
            print(content)
        except Exception as e:
            print(e)
    http_request(url)

