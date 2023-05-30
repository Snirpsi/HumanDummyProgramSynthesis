#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that opens a http request.
    while True:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cells = [c.get_text() for c in cols]
            print(cells)
        time.sleep(1)

