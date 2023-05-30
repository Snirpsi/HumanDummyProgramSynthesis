#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    def http_get(url):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_post(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_put(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_del(url):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_head(url):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_options(url):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_head(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_options(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_put(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_del(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_head(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_options(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_put(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0')
            resp = urllib.request.urlopen(req,data)
            return resp.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that opens a http request.
    def http_del(url,data):
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: