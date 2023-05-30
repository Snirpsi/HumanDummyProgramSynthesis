#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that stores a http request.
    while True:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', {'class': 'title'})
        title = title.text
        print(title)
        time.sleep(1)

