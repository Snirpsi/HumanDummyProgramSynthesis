#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('a'):
        print(link.get('href'))

