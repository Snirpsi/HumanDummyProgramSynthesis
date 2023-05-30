#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    #The request is sent to the url specified in the command line arguments.
    #The response is printed to the screen.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read())

