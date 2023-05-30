#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that stores a http request.
    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0')
    request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Language', 'en-US,en;q=0.5')
    request.add_header('Accept-Encoding', 'gzip, deflate')
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', 'snirps.ddns.net')
    request.add_header('Referer', 'http://snirps.ddns.net')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    request.add_header('Content-Length', '7')
    request.add_header('Cookie', '__cfduid=d1d7d18b00b20e00b00b00b00b00b00b00b00b; __utma=715348247.15348247.15348247.15348247; __utmc=715348247; __utmz=715348247.15348247.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)')
    response = urllib.request.urlopen(request)
    print(response.read())

