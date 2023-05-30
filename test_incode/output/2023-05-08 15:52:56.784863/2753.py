#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that requests a http request.
    #The request is made using the requests library.
    #The response is then returned to the caller.
    req = requests.get(url)
    print(req.status_code)
    print(req.text)

