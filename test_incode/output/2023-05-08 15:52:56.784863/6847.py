#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that requests a http request.
    while True:
        req = requests.get(url)
        req.raise_for_status()
        print(req.status_code)
        print(req.text)
        time.sleep(1)

