#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    #It will print the response code and the response body.
    #The response code will be 200 if the request was successful.
    #The response body will be the response body.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.code)
    print(response.read().decode('utf-8'))

