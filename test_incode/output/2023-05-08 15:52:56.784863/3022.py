#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that calculates a http request.
    while True:
        request = requests.get(url)
        print(request.status_code)
        time.sleep(1)

