#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that enumerates a http request.
    #It will print out the url and the response code.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))

