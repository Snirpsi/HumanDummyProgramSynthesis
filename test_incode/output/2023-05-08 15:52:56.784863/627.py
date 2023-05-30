#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that converts a http request.
    while True:
        request = requests.get(url)
        request.raise_for_status()
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1')
        title = title.text
        title = title.strip()
        title = title.title()
        print(title)
        time.sleep(1)

