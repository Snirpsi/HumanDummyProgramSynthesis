#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that converts a http request.
    #The program will print out the response from the server.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read())

