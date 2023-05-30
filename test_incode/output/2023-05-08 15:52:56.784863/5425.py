#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    #It will return the response from the server.
    #It will also print the response to the screen.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())

