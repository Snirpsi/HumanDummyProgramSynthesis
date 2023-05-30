#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that iterates over a http request.
    #The request is made using urllib2.urlopen.
    #The response is returned as a string.
    #The response is then decoded using utf-8.
    #The response is then printed using print.
    response = urllib.request.urlopen(url)
    response_str = response.read().decode("utf-8")
    print(response_str)
    response.close()

