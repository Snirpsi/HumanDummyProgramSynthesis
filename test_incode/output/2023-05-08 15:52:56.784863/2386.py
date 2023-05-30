#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    #The request is sent to the url and receives a response.
    #The response is then parsed and printed out.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    print(html)

