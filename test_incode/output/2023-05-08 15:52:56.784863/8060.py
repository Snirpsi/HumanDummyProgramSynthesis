#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that enumerates a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        for link in soup.find_all('a'):
            print(link.get('href'))
        time.sleep(1)

