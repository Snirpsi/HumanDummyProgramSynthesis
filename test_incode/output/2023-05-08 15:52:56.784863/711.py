#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that iterates over a http request.
    #The request is made using urllib2.urlopen.
    #The response is returned as a string.
    #The response is then parsed and returned.
    #The response is then printed out.
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    response_str = response.read()
    print(response_str)
    
    

