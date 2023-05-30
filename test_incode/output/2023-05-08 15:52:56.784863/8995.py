#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that returns a http request.
    #The request is sent to the url and returns the response.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read())

