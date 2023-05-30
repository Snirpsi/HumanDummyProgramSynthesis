#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that stores a http request.
    while True:
        req = requests.get(url)
        if req.status_code == 200:
            print(req.status_code)
            print(req.text)
        else:
            print("Error code:", req.status_code)
            print("Error message:", req.text)
        time.sleep(5)

