#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that prints a http request.
    while True:
        try:
            req = requests.get(url)
            print(req.status_code)
            print(req.text)
        except:
            print("Connection failed")
            time.sleep(5)

