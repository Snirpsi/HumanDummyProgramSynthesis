#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that adds a http request.
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    urllib.request.urlopen(req)

