#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
            urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            print(e)
            time.sleep(1)

