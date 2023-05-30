#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that requests a http request.
    #It returns the response as a string.
    #The response is automatically decoded.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read())

