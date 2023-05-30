#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that calculates a http request.
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    req.add_header('Accept-Language', 'en-US,en;q=0.8')
    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)

