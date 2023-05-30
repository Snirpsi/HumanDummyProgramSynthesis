#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that removes a http request.
    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0')
    response = urllib.request.urlopen(request)
    print(response.read())

