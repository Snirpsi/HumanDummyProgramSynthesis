#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that stores a http request.
    while True:
        req = requests.get(url)
        print(req.status_code)
        print(req.text)
        time.sleep(1)

