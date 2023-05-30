#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that converts a http request.
    #The request is sent to the url and receives a response.
    #The response is then converted into a string and printed.
    #The program is then terminated.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read()
    print(content)
    
    
    

