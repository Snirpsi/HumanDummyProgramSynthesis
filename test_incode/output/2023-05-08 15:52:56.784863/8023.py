#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that prints a http request.
    def print_request(url):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
            resp = urllib.request.urlopen(req)
            content = resp.read()
            print(content)
        except Exception as e:
            print(e)
    print_request(url)

