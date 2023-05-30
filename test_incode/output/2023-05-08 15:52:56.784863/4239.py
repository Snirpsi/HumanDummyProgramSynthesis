#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        try:
            req = urllib.request.Request(url)
            urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            print(e)
            break

