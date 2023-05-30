#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that calculates a http request.
    def http_request(url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return response.read()
    #The main function that runs the program.
    content = http_request(url)
    print(content)

