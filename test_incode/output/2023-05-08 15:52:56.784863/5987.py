#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that opens a http request.
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
    response = urllib.request.urlopen(req)
    print(response.read())

