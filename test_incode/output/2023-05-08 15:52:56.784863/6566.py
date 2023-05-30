#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that prints a http request.
    def http_request(url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        print(response.read())
    http_request(url)

