#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that opens a http request.
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Cache-Control', 'max-age=0')
    req.add_header('Host', 'snirps.ddns.net')
    req.add_header('Referer', 'http://snirps.ddns.net/')
    req.add_header('Upgrade-Insecure-Requests', '1')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Content-Length', '0')
    req.add_header('Connection', 'close')
    req.add_header('Cookie', 'PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9f507dccb; PHPSESSID=7dccb5b9cffbfe9d07e3ba9

