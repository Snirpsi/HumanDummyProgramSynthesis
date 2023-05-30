#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        try:
            req = requests.get(url)
            req.close()
        except:
            pass
        time.sleep(5)

