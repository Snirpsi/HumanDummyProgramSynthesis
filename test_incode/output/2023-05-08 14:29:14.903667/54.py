#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that calculates a http request.
    #The request is sent to the url and returns the response.
    #The response is then parsed using beautiful soup.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.prettify())

