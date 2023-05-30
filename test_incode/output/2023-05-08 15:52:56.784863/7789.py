#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        req = requests.get(url)
        if req:
            req.close()
            break
        time.sleep(1)

