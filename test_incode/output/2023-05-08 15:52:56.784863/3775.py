#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        req = requests.get(url)
        if req.status_code == 200:
            req.close()
        else:
            print("Error connecting to server.")
            break

