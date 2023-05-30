#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that enumerates a http request.
    import sys
    
    #Get the url from the command line.
    url = sys.argv[1]
    
    #Get the request from the url.
    request = requests.get(url)
    
    #Print the request headers.
    print(request.headers)
    
    #Print the request body.
    print(request.text)

