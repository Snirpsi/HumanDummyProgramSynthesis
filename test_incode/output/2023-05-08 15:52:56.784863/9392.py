#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    #The function returns a string with the response.
    #The function also prints the response to the console.
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.read())

