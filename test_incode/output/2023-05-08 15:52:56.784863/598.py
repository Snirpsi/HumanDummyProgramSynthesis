#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        try:
            req = requests.get(url)
            req.raise_for_status()
            url = req.url
        except requests.exceptions.RequestException as e:
            print(e)
            time.sleep(1)
            continue

