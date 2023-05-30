#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that removes a http request.
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    urllib.request.urlopen(req)
    #A program that prints out the contents of a file.
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print(html)

