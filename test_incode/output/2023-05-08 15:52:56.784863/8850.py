#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    #The request is made using urllib2.
    #The response is then converted into a string.
    #The string is then printed out to the screen.
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()
    print(content)

