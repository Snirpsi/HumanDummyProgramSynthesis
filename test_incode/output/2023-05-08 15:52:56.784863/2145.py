#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that opens a http request.
    while True:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        print(response.read().decode())
        time.sleep(1)

