#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that enumerates a http request.
    #It will print out all the headers and body of the request.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.info())
    print(response.read())

