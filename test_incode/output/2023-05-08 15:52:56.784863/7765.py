#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that stores a http request.
    #It then prints the response from the server.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())

