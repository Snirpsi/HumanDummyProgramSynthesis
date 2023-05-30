#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that converts a http request.
    while True:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = response.read()
        print(data)
        time.sleep(1)

