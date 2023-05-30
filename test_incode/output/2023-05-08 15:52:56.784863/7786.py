#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that stores a http request.
    def http_request_handler(request):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return response.read()
    #A function that stores a http response.
    def http_response_handler(response):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'text/html')
        req.add_header('Content-Length', str(len(response)))
        req.add_header('Connection', 'close')
        urllib.request.urlopen(req, response).read()
    #A function that stores a http response.
    def http_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_404_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_500_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_502_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_503_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_504_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_505_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_506_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_507_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_508_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_511_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_500_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_502_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_503_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_504_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_505_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_506_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_error_507_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def 

