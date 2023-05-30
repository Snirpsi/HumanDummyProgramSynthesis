#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that stores a http request.
    def http_request(url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores a response from the http request.
    def http_response(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_json(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_text(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'text/plain')
        req.add_header('Accept', 'text/plain')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_xml(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/xml')
        req.add_header('Accept', 'application/xml')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_json(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_text(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'text/plain')
        req.add_header('Accept', 'text/plain')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_xml(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/xml')
        req.add_header('Accept', 'application/xml')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_json(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_text(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'text/plain')
        req.add_header('Accept', 'text/plain')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_xml(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/xml')
        req.add_header('Accept', 'application/xml')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_json(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores the response from the http request.
    def http_response_text(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'text/plain')
        req.add_header('Accept

