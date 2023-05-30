#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that calculates a http request.
    while True:
        req = requests.get(url)
        print(req.status_code)
        if req.status_code == 200:
            break
        else:
            print("Error connecting to server")

