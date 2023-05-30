#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that removes a http request.
    def http_request(url):
        try:
            req = urllib.request.Request(url)
            urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            print(e)
        except urllib.error.URLError as e:
            print(e)
    http_request(url)

