#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
        time.sleep(1)

