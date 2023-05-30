#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that returns a http request.
    def request():
        return requests.get(url)
    #A function that returns a json response.
    def response():
        return requests.get(url).json()
    #A function that returns a text response.
    def response():
        return requests.get(url).text
    #A function that returns a file response.
    def response():
        return requests.get(url).content
    #A function that returns a file response.
    def response():
        return requests.get(url).file

