#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that stores a http request.
    def http_request(url):
        try:
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_code(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            code = resp.getcode()
            return code
        except:
            return "error"
    #A function that stores a http response.
    def http_response_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            header = resp.getallheaders()
            return header
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_code(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            code = resp.getcode()
            return code
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            header = resp.getallheaders()
            return header
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_code(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            code = resp.getcode()
            return code
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            header = resp.getallheaders()
            return header
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_headers_code(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            code = resp.getcode()
            return code
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_headers_headers_headers(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            header = resp.getallheaders()
            return header
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_headers_headers_headers_content(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            return content
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_headers_headers_headers_headers_headers(content):
        try:
            resp = urllib.request.urlopen(content)
            content = resp.read()
            header = resp.getallheaders()
            return header
        except:
            return "error"
    #A function that stores a http response.
    def http_response_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_headers_header

