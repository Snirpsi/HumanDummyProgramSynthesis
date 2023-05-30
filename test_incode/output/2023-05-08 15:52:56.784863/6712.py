#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that opens a http request.
    while True:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept-Language', 'en-US,en;q=0.8')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Host', 'snirps.ddns.net')
        req.add_header('Referer', 'http://snirps.ddns.net')
        req.add_header('Upgrade-Insecure-Requests', '1')
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        req.add_header('Cache-Control', 'no-cache')
        req.add_header('Cookie', '__cfduid=d15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15b54e15

