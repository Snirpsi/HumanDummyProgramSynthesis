#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that enumerates a http request.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        print(link.get("href"))

