#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        title = soup.find('h1', {'class': 'title'})
        print(title.text)
        time.sleep(1)

