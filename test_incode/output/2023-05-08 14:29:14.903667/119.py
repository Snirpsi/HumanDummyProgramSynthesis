#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that converts a http request.
    while True:
        try:
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            page = resp.read()
            soup = BeautifulSoup(page, 'html.parser')
            title = soup.find('h1')
            print(title.text)
        except urllib.error.URLError as e:
            print(e)
            break

