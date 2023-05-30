#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that stores a http request.
    while True:
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, "html.parser")
        title = soup.find("h1", {"class": "title"}).text
        print(title)
        time.sleep(1)

