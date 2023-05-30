#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that returns a http request.
    #The request is made using urllib2.
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print(response.read())

