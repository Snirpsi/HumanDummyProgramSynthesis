#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    #The request is sent to the url and returns the response.
    #The response is then printed to the screen.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())

