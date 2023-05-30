#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that requests a http request.
    while True:
        try:
            req = requests.get(url)
            req.raise_for_status()
            soup = BeautifulSoup(req.content, 'html.parser')
            title = soup.find('h1', {'class': 'title'})
            print(title.text)
        except requests.exceptions.RequestException as e:
            print(e)

