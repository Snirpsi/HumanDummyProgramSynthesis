#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that iterates over a http request.
    #It will print out the response from the server
    def iterate_over_request(url, headers):
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read()
        print(html)
    iterate_over_request(url, headers)

