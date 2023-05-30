#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that calculates a http request.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read())

