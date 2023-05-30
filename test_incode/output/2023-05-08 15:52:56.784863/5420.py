#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        title = soup.find('h1', {'class': 'title'})
        title = title.text
        print(title)
        time.sleep(1)

