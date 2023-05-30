#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    #It then prints the response body to the terminal.
    #The program will exit if the request fails.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))

