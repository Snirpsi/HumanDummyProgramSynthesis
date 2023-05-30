#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that requests a http request.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())

