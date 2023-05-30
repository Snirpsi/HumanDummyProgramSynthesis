#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that returns a http request.
    while True:
        try:
            req = requests.get(url)
            req.raise_for_status()
            print(req.status_code)
            print(req.text)
            break
        except requests.exceptions.RequestException as e:
            print(e)
            time.sleep(5)

