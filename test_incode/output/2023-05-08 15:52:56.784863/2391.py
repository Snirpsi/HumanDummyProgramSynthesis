#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that enumerates a http request.
    while True:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        html = response.read()
        print(html)
        time.sleep(1)

