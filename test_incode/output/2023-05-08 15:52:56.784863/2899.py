#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that opens a http request.
    while True:
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
            resp = urllib.request.urlopen(req)
            html = resp.read()
            print(html)
            break
        except urllib.error.URLError as e:
            print(e)
            time.sleep(5)

