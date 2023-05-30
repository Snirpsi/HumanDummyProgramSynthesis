#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', {'class': 'title'})
        print(title.text)
        time.sleep(1)

