#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that calculates a http request.
    while True:
        req = requests.get(url)
        if req.status_code == 200:
            print(req.text)
        else:
            print("HTTP request failed")
        time.sleep(1)

