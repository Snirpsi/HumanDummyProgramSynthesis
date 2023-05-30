#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that enumerates a http request.
    def enumerate_request(request):
        request = urllib.request.Request(url)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlopen(request)
    enumerate_request(url)

