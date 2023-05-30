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
    def http_server_handler(server):
        print("Serving on", server.socket.getsockname())
    #A function that stores a http response.
    def http_server_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_error_handler(error):
        print("Error code:", error.code)
        print("Reason:", error.reason)
        print("URL:", error.url)
        print("Headers:", error.headers)
        print("Body:", error.body)
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_handler(server):
        print("Shutting down")
    #A function that stores a http response.
    def http_server_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown_shutdown

