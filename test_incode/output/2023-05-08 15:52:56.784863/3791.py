#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        try:
            req = requests.get(url)
            req.raise_for_status()
        except requests.exceptions.HTTPError:
            print("HTTP error")
        except requests.exceptions.RequestException:
            print("Request error")
        else:
            print(req.text)
            break

