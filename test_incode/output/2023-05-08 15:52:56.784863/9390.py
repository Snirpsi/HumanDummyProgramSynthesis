#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that calculates a http request.
    while True:
        req = requests.get(url)
        req.raise_for_status()
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title')
        print(title.text)
        time.sleep(1)

