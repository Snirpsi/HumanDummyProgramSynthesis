#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that requests a http request.
    #The request is made asynchronously.
    #The response is returned to the caller.
    #The request is made synchronously.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())

