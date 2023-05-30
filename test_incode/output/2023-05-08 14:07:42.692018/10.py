#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that converts a http request.
    while True:
        try:
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            html = resp.read()
            print(html)
        except urllib.error.URLError as e:
            print(e)
        except urllib.error.HTTPError as e:
            print(e)
        except urllib.error.ReadError as e:
            print(e)
        except KeyboardInterrupt:
            break
