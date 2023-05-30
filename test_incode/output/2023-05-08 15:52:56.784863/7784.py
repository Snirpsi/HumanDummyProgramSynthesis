#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that stores a http request.
    while True:
        try:
            req = requests.get(url)
            req.raise_for_status()
            soup = BeautifulSoup(req.text, "html.parser")
            links = soup.find_all("a")
            for link in links:
                print(link.get("href"))
        except:
            break

